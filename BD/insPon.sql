-- Insertions générées par ChatGPT, puis modifiées pour correspondre à nos souhaits

-- Ajout de personnes 
INSERT INTO PERSONNE VALUES (1, 'Dupont', 'Jean', 'jean.dupont@mail.com', 70); -- Adhérent
INSERT INTO PERSONNE VALUES (2, 'Martin', 'Alice', 'alice.martin@mail.com', 60); -- Moniteur
INSERT INTO PERSONNE VALUES (3, 'Durand', 'Sophie', 'sophie.durand@mail.com', 120); -- Adhérent
INSERT INTO PERSONNE VALUES (4, 'Petit', 'Lucas', 'lucas.petit@mail.com', 50); -- Poney compatible
INSERT INTO PERSONNE VALUES (5, 'Moreau', 'Léo', 'leo.moreau@mail.com', 40); -- Poney incompatible
INSERT INTO PERSONNE VALUES (6, 'Paire', 'Tom', 'tom.paire@mail.com', 45); -- Moniteur

-- Adhérent déjà Moniteur
INSERT INTO MONITEUR VALUES (2); -- Alice devient moniteur
-- INSERT INTO ADHERENT VALUES (2, TRUE); -- Devrait échouer (validé)

-- Moniteur déjà Adhérent
INSERT INTO ADHERENT VALUES (1, TRUE); -- Jean devient adhérent
-- INSERT INTO MONITEUR VALUES (1); -- Devrait échouer (validé)

-- Ajout de poneys et cours
INSERT INTO PONEY VALUES (101, 'Tonerre', 80);
INSERT INTO PONEY VALUES (102, 'Berry', 60);

INSERT INTO MONITEUR VALUES (6); -- Tom devient moniteur
INSERT INTO COURS VALUES (201, 2, 2, '2024-11-25 10:00:00', 1, 50.00);
INSERT INTO COURS VALUES (202, 6, 2, '2024-11-25 10:30:00', 2, 75.00);

-- Horaire du moniteur indisponible
-- INSERT INTO COURS VALUES (203, 2, 2, '2024-11-25 10:30:00', 1, 50.00); -- Devrait échouer (validé)

-- Ajout de participations de poneys
INSERT INTO PARTICIPER VALUES (201, 101); -- Poney 101 participe au cours 201
-- INSERT INTO PARTICIPER VALUES (202, 101); -- Devrait échouer (validé)

-- Repos insuffisant pour le poney
INSERT INTO COURS VALUES (204, 2, 2, '2024-11-25 14:00:00', 1, 50.00);
-- INSERT INTO PARTICIPER VALUES (204, 101); -- Devrait échouer (validé)

-- Inscription d'adhérents à des cours
INSERT INTO ADHERENT VALUES (4, FALSE); -- Sophie est adhérente mais n'a pas payée sa cotisation
-- INSERT INTO INSCRIRE VALUES (201, 4, FALSE); -- Devrait échouer (cotisation non payée) (validé)

INSERT INTO INSCRIRE VALUES (201, 1, TRUE); -- Jean s'inscrit
-- INSERT INTO INSCRIRE VALUES (201, 5, TRUE); -- Devrait échouer (cours complet) (validé)

-- INSERT INTO INSCRIRE VALUES (202, 3, TRUE); -- Devrait échouer (poids trop élevé pour les poneys) (validé)