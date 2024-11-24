-- creation des tables de la BD Poney

CREATE TABLE PERSONNE(
    idPers INT(8) PRIMARY KEY,
    nomPers VARCHAR(42),
    prenomPers VARCHAR(42),
    mailPers VARCHAR(42),
    poidsPers INT(3)
);

CREATE TABLE ADHERENT(
    idAdh INT(8),
    cotisationPaye BOOLEAN,
    PRIMARY KEY (idAdh)
);

CREATE TABLE MONITEUR(
    idMon INT(8),
    PRIMARY KEY (idMon)
);

CREATE TABLE PONEY(
    idPon INT(8) PRIMARY KEY,
    nomPon VARCHAR(42),
    poidsMax INT(3)
);

CREATE TABLE COURS(
    idCours INT(8) PRIMARY KEY,
    idMon INT(8),
    nbPersMax INT(2),
    dateCou DATETIME,
    duree INT(1),
    prixCou DECIMAL(5,2),
    check (duree between 1 and 2),
    check (nbPersMax between 1 and 10)
);

CREATE TABLE PARTICIPER(
    idCours INT(8),
    idPon INT(8),
    PRIMARY KEY (idCours, idPon)
);

CREATE TABLE INSCRIRE(
    idCours INT(8),
    idAdh INT(8),
    paye BOOLEAN
);

-- creation des clés etrangères de la BD Poney

ALTER TABLE ADHERENT ADD FOREIGN KEY (idAdh) REFERENCES PERSONNE(idPers);
ALTER TABLE MONITEUR ADD FOREIGN KEY (idMon) REFERENCES PERSONNE(idPers);
ALTER TABLE COURS ADD FOREIGN KEY (idMon) REFERENCES MONITEUR(idMon);
ALTER TABLE PARTICIPER ADD FOREIGN KEY (idCours) REFERENCES COURS(idCours);
ALTER TABLE PARTICIPER ADD FOREIGN KEY (idPon) REFERENCES PONEY(idPon);
ALTER TABLE INSCRIRE ADD FOREIGN KEY (idCours) REFERENCES COURS(idCours);
ALTER TABLE INSCRIRE ADD FOREIGN KEY (idAdh) REFERENCES ADHERENT(idAdh);

-- creation des triggers de la BD Poney

delimiter |
create or replace trigger estDejaMonit before insert on ADHERENT for each row
begin
    if exists (
        select idMon
        from MONITEUR 
        where idMon = new.idAdh
    ) then
        SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = 'La personne est déjà un moniteur !';
    end if;
end |

create or replace trigger estDejaMonit before update on ADHERENT for each row
begin
    if exists (
        select idMon
        from MONITEUR 
        where idMon = new.idAdh
    ) then
        SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = 'La personne est déjà un moniteur !';
    end if;
end |

create or replace trigger estDejaAdher before insert on MONITEUR for each row
begin
    if exists (
        select idAdh
        from ADHERENT 
        where idAdh = new.idMon
    ) then
        SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = 'La personne est déjà un adhérant !';
    end if;
end |

create or replace trigger estDejaAdher before update on MONITEUR for each row
begin
    if exists (
        select idAdh
        from ADHERENT 
        where idAdh = new.idMon
    ) then
        SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = 'La personne est déjà un adhérant !';
    end if;
end |

create or replace trigger disponibiliteMoniteur before insert on COURS for each row
begin
    declare mes varchar(128);

    if exists (
        select idCours
        from COURS
        where idMon = new.idMon
            and (
                new.dateCou between dateCou and DATE_ADD(dateCou, INTERVAL duree HOUR)
                or dateCou between new.dateCou and DATE_ADD(new.dateCou, INTERVAL new.duree HOUR)
            )
    ) then
        set mes = CONCAT("Le moniteur a déjà un cours pendant cet horaire.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |

create or replace trigger disponibiliteMoniteur before update on COURS for each row
begin
    declare mes varchar(128);

    if exists (
        select idCours
        from COURS
        where idMon = new.idMon
            and (
                new.dateCou between dateCou and DATE_ADD(dateCou, INTERVAL duree HOUR)
                or dateCou between new.dateCou and DATE_ADD(new.dateCou, INTERVAL new.duree HOUR)
            )
    ) then
        set mes = CONCAT("Le moniteur a déjà un cours pendant cet horaire.");
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
end |

create or replace trigger verifierInscription before insert on INSCRIRE for each row
begin
    declare nbMax int;
    declare nbParticip int;

    declare cotiPaye boolean;

    declare nbPoney int;
    
    declare mes varchar(1024) default '';

    -- Vérification 1 : Cours complet

    select nbPersMax into nbMax 
    from COURS 
    where idCours = new.idCours;

    select count(idAdh) into nbParticip 
    from INSCRIRE 
    where idCours = new.idCours;

    if nbParticip + 1 > nbMax then
        set mes = concat(mes, "Impossible de rejoindre le cours ", new.idCours, ", car il est complet !\n");
    end if;

    -- Vérification 2 : Cotisation non payée

    select cotisationPaye into cotiPaye 
    from ADHERENT 
    where idAdh = new.idAdh;

    if not cotiPaye then
        set mes = concat(mes, "Cet adhérent n'a pas payé sa cotisation, il ne peut pas s'inscrire à un cours !\n");
    end if;

    -- Vérification 3 : Poids non supporté par les poneys

    select count(idPon) into nbPoney
    from PERSONNE NATURAL JOIN ADHERENT NATURAL JOIN INSCRIRE NATURAL JOIN COURS NATURAL JOIN PARTICIPER NATURAL JOIN PONEY
    where idCours = new.idCours and poidsPers > poidsMax;

    if nbPoney > 0 then
        set mes = concat(mes, "Impossible d'ajouter l'adhérent, le cours ", new.idCours, " ne contient aucun poney pouvant supporter son poids !\n");
    end if;

    -- Envoi du message d'erreur

    if mes != '' then
        signal SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    end if;
end |

create or replace trigger verifierInscription before update on INSCRIRE for each row
begin
    declare nbMax int;
    declare nbParticip int;

    declare cotiPaye boolean;

    declare nbPoney int;
    
    declare mes varchar(1024) default '';

    -- Vérification 1 : Cours complet

    select nbPersMax into nbMax 
    from COURS 
    where idCours = new.idCours;

    select count(idAdh) into nbParticip 
    from INSCRIRE 
    where idCours = new.idCours;

    if nbParticip + 1 > nbMax then
        set mes = concat(mes, "Impossible de rejoindre le cours ", new.idCours, ", car il est complet !\n");
    end if;

    -- Vérification 2 : Cotisation non payée

    select cotisationPaye into cotiPaye 
    from ADHERENT 
    where idAdh = new.idAdh;

    if not cotiPaye then
        set mes = concat(mes, "Cet adhérent n'a pas payé sa cotisation, il ne peut pas s'inscrire à un cours !\n");
    end if;

    -- Vérification 3 : Poids non supporté par les poneys

    select count(idPon) into nbPoney
    from PERSONNE NATURAL JOIN ADHERENT NATURAL JOIN INSCRIRE NATURAL JOIN COURS NATURAL JOIN PARTICIPER NATURAL JOIN PONEY
    where idCours = new.idCours and poidsPers > poidsMax;

    if nbPoney > 0 then
        set mes = concat(mes, "Impossible d'ajouter l'adhérent, le cours ", new.idCours, " ne contient aucun poney pouvant supporter son poids !\n");
    end if;

    -- Envoi du message d'erreur

    if mes != '' then
        signal SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    end if;
end |

create or replace trigger verifierParticiper before insert on PARTICIPER for each row
begin
    declare mes varchar(1024) default '';
    
    declare newDateCou datetime;
    declare newDuree int;

    declare debutDernierCours datetime default null;
    declare dureeDernierCours int default 0;
    declare reposNecessaire int default 0;
    declare reposEffectif int default 0;

    -- Récupère le nouveau cours
    select COURS.dateCou, COURS.duree 
    into newDateCou, newDuree
    from COURS
    where COURS.idCours = new.idCours;

    -- Récupère le dernier cours
    select COURS.dateCou, COURS.duree 
    into debutDernierCours, dureeDernierCours
    from COURS 
    join PARTICIPER on COURS.idCours = PARTICIPER.idCours
    where PARTICIPER.idPon = new.idPon
    order by COURS.dateCou desc
    limit 1;

    if debutDernierCours is not null then
        -- Calcul du temps de repos nécessaire (30min pour 1h, 1h pour 2h)
        set reposNecessaire = dureeDernierCours * 30; -- en minutes
        
        -- Calcul du temps de repos effectif entre les deux cours
        set reposEffectif = TIMESTAMPDIFF(MINUTE, 
            TIMESTAMPADD(MINUTE, dureeDernierCours * 60, debutDernierCours), -- fin du dernier cours
            newDateCou -- début du nouveau cours
        );
        
        if reposEffectif < reposNecessaire then
            set mes = CONCAT("Le poney ", new.idPon, " n'a pas assez de repos (manque ", 
                reposNecessaire - reposEffectif, " minutes). Il faut ", 
                reposNecessaire, " minutes de repos après un cours de ", 
                dureeDernierCours, " heure(s).");
            SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = mes;
        end if;
    end if;
end |

create or replace trigger verifierParticiper before update on PARTICIPER for each row
begin
    declare mes varchar(1024) default '';
    
    declare newDateCou datetime;
    declare newDuree int;

    declare debutDernierCours datetime default null;
    declare dureeDernierCours int default 0;
    declare reposNecessaire int default 0;
    declare reposEffectif int default 0;

    -- Récupère le nouveau cours
    select COURS.dateCou, COURS.duree 
    into newDateCou, newDuree
    from COURS
    where COURS.idCours = new.idCours;

    -- Récupère le dernier cours
    select COURS.dateCou, COURS.duree 
    into debutDernierCours, dureeDernierCours
    from COURS 
    join PARTICIPER on COURS.idCours = PARTICIPER.idCours
    where PARTICIPER.idPon = new.idPon
    order by COURS.dateCou desc
    limit 1;

    if debutDernierCours is not null then
        -- Calcul du temps de repos nécessaire (30min pour 1h, 1h pour 2h)
        set reposNecessaire = dureeDernierCours * 30; -- en minutes
        
        -- Calcul du temps de repos effectif entre les deux cours
        set reposEffectif = TIMESTAMPDIFF(MINUTE, 
            TIMESTAMPADD(MINUTE, dureeDernierCours * 60, debutDernierCours), -- fin du dernier cours
            newDateCou -- début du nouveau cours
        );
        
        if reposEffectif < reposNecessaire then
            set mes = CONCAT("Le poney ", new.idPon, " n'a pas assez de repos (manque ", 
                reposNecessaire - reposEffectif, " minutes). Il faut ", 
                reposNecessaire, " minutes de repos après un cours de ", 
                dureeDernierCours, " heure(s).");
            SIGNAL SQLSTATE '45000' set MESSAGE_TEXT = mes;
        end if;
    end if;
end |

delimiter ;