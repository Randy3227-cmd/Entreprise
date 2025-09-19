-- =========================
-- Développeur
-- =========================
INSERT INTO Question (question, point) VALUES
('Quel langage est le plus utilise pour Android ?', 2),
('Que signifie CSS ?', 2),
('Quel est le role principal d''un framework ?', 2),
('Que fait une base de donnees relationnelle ?', 2),
('Quel outil est utilise pour gerer les versions de code ?', 2);

INSERT INTO Reponse (reponse) VALUES
('Java'), 
('Python'), 
('C#'),                            -- Q1
('Cascading Style Sheets'), 
('Creative Style System'), 
('Code Styling Structure'), -- Q2
('Accelerer le developpement avec des outils prets'), 
('Remplacer le langage de programmation'), 
('Creer uniquement des interfaces graphiques'), -- Q3
('Stocker et organiser des donnees en tables'), 
('Compiler du code plus rapidement'), 
('Creer des interfaces utilisateur dynamiques'), -- Q4
('Git'), 
('Docker'), 
('Jenkins');                        -- Q5

-- Liaisons
INSERT INTO Question_reponse (id_question, id_reponse) VALUES
(1,1),(1,2),(1,3),
(2,4),(2,5),(2,6),
(3,7),(3,8),(3,9),
(4,10),(4,11),(4,12),
(5,13),(5,14),(5,15);

-- Bonnes réponses
INSERT INTO Correct_reponse (id_question, id_reponse) VALUES
(1,1),(2,4),(3,7),(4,10),(5,13);


-- =========================
-- Chef de projet
-- =========================
INSERT INTO Question (question, point) VALUES
('Quelle methode agile est la plus populaire ?', 2),
('Quel document decrit les taches dans Scrum ?', 2),
('Quel est le role principal d''un chef de projet ?', 2),
('Que represente un diagramme de Gantt ?', 2),
('Que signifie MVP en gestion de projet ?', 2);

INSERT INTO Reponse (reponse) VALUES
('Scrum'), ('Kanban'), ('Waterfall'),               -- Q6
('Product Backlog'), ('Kanban Board'), ('Roadmap'), -- Q7
('Coordonner et superviser l''avancement'), ('Ecrire du code'), ('Concevoir le produit seul'), -- Q8
('La duree des taches'), ('Le budget total'), ('La structure du code'), -- Q9
('Minimum Viable Product'), ('Most Valuable Plan'), ('Managed Vision Project'); -- Q10

-- Liaisons
INSERT INTO Question_reponse (id_question, id_reponse) VALUES
(6,16),(6,17),(6,18),
(7,19),(7,20),(7,21),
(8,22),(8,23),(8,24),
(9,25),(9,26),(9,27),
(10,28),(10,29),(10,30);

-- Bonnes réponses
INSERT INTO Correct_reponse (id_question, id_reponse) VALUES
(6,16),(7,19),(8,22),(9,25),(10,28);


-- =========================
-- Designer UX/UI
-- =========================
INSERT INTO Question (question, point) VALUES
('Quel est l''objectif de l''UX design ?', 2),
('Quel outil est le plus utilise pour les maquettes interactives ?', 2),
('Quelle est la difference entre UI et UX ?', 2),
('Quelle couleur est souvent associee a la confiance ?', 2),
('Quel est le principe cle du design centre utilisateur ?', 2);

INSERT INTO Reponse (reponse) VALUES
('Ameliorer l''experience utilisateur'), ('Creer des bases de donnees'), ('Optimiser le backend'), -- Q11
('Figma'), ('Excel'), ('Docker'), -- Q12
('UI = interface, UX = experience'), ('UI = experience, UX = interface'), ('C''est la meme chose'), -- Q13
('Bleu'), ('Rouge'), ('Jaune'), -- Q14
('Prendre en compte les besoins des utilisateurs'), ('Reduire le temps de developpement'), ('Optimiser le SEO'); -- Q15

-- Liaisons
INSERT INTO Question_reponse (id_question, id_reponse) VALUES
(11,31),(11,32),(11,33),
(12,34),(12,35),(12,36),
(13,37),(13,38),(13,39),
(14,40),(14,41),(14,42),
(15,43),(15,44),(15,45);

-- Bonnes réponses
INSERT INTO Correct_reponse (id_question, id_reponse) VALUES
(11,31),(12,34),(13,37),(14,40),(15,43);


-- =========================
-- Analyste financier
-- =========================
INSERT INTO Question (question, point) VALUES
('Que mesure le ratio PER ?', 2),
('Que contient le rapport annuel ?', 2),
('Quel indicateur mesure la rentabilite ?', 2),
('Quelle est la monnaie officielle de la zone euro ?', 2),
('Quel outil est utilise pour analyser des donnees financieres ?', 2);

INSERT INTO Reponse (reponse) VALUES
('La rentabilite des actions'), ('La solvabilite'), ('Les dividendes'), -- Q16
('Bilan et compte de resultat'), ('Plan marketing'), ('Organigramme'), -- Q17
('ROI (Return On Investment)'), ('CTR (Click Through Rate)'), ('CPC (Cost Per Click)'), -- Q18
('Euro'), ('Dollar'), ('Livre Sterling'), -- Q19
('Excel'), ('Photoshop'), ('Word'); -- Q20

-- Liaisons
INSERT INTO Question_reponse (id_question, id_reponse) VALUES
(16,46),(16,47),(16,48),
(17,49),(17,50),(17,51),
(18,52),(18,53),(18,54),
(19,55),(19,56),(19,57),
(20,58),(20,59),(20,60);

-- Bonnes réponses
INSERT INTO Correct_reponse (id_question, id_reponse) VALUES
(16,46),(17,49),(18,52),(19,55),(20,58);


-- =========================
-- Responsable marketing
-- =========================
INSERT INTO Question (question, point) VALUES
('Quel indicateur mesure le taux de clic ?', 2),
('Quel est le but d''une etude de marche ?', 2),
('Que signifie SEO ?', 2),
('Quel canal est le plus utilise pour le marketing digital ?', 2),
('Que signifie KPI ?', 2);

INSERT INTO Reponse (reponse) VALUES
('CTR (Click Through Rate)'), ('ROI (Return On Investment)'), ('CPC (Cost Per Click)'), -- Q21
('Connaitre les besoins des clients'), ('Optimiser le code produit'), ('Augmenter la vitesse du site'), -- Q22
('Search Engine Optimization'), ('Systematic Engagement Option'), ('Social Engagement Organization'), -- Q23
('Reseaux sociaux'), ('Intranet'), ('Television uniquement'), -- Q24
('Key Performance Indicator'), ('Knowledge Process Insight'), ('Kind Product Innovation'); -- Q25

-- Liaisons
INSERT INTO Question_reponse (id_question, id_reponse) VALUES
(21,61),(21,62),(21,63),
(22,64),(22,65),(22,66),
(23,67),(23,68),(23,69),
(24,70),(24,71),(24,72),
(25,73),(25,74),(25,75);

-- Bonnes réponses
INSERT INTO Correct_reponse (id_question, id_reponse) VALUES
(21,61),(22,64),(23,67),(24,70),(25,73);


-- =========================
-- Tests (un test par poste)
-- =========================
INSERT INTO Test (nom) VALUES
('QCM Developpeur'),
('QCM Chef de projet'),
('QCM Designer UX/UI'),
('QCM Analyste financier'),
('QCM Responsable marketing');

INSERT INTO test_question (id_question, id_test) VALUES (1,1);
INSERT INTO test_question (id_question, id_test) VALUES (2,1);
INSERT INTO test_question (id_question, id_test) VALUES (3,1);
INSERT INTO test_question (id_question, id_test) VALUES (4,1);
INSERT INTO test_question (id_question, id_test) VALUES (5,1);

INSERT INTO test_question (id_question, id_test) VALUES (6,2);
INSERT INTO test_question (id_question, id_test) VALUES (7,2);
INSERT INTO test_question (id_question, id_test) VALUES (8,2);
INSERT INTO test_question (id_question, id_test) VALUES (9,2);
INSERT INTO test_question (id_question, id_test) VALUES (10,2);

INSERT INTO test_question (id_question, id_test) VALUES (11,3);
INSERT INTO test_question (id_question, id_test) VALUES (12,3);
INSERT INTO test_question (id_question, id_test) VALUES (13,3);
INSERT INTO test_question (id_question, id_test) VALUES (14,3);
INSERT INTO test_question (id_question, id_test) VALUES (15,3);

INSERT INTO test_question (id_question, id_test) VALUES (16,4);
INSERT INTO test_question (id_question, id_test) VALUES (17,4);
INSERT INTO test_question (id_question, id_test) VALUES (18,4);
INSERT INTO test_question (id_question, id_test) VALUES (19,4);
INSERT INTO test_question (id_question, id_test) VALUES (20,4);

INSERT INTO test_question (id_question, id_test) VALUES (21,5);
INSERT INTO test_question (id_question, id_test) VALUES (22,5);
INSERT INTO test_question (id_question, id_test) VALUES (23,5);
INSERT INTO test_question (id_question, id_test) VALUES (24,5);
INSERT INTO test_question (id_question, id_test) VALUES (25,5);
