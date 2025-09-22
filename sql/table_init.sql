
-- ===================================
-- Création des tables principales
-- ===================================

CREATE TABLE Formation (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE Competence (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE Langue (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE Loisir (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE Candidat (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telephone VARCHAR(30),
    date_naissance DATE,
    adresse VARCHAR(255)
);

CREATE TABLE CV (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(150) NOT NULL,
    resume TEXT,
    date_creation DATE DEFAULT CURRENT_DATE,
    id_candidat INT NOT NULL,
    CONSTRAINT fk_cv_candidat FOREIGN KEY (id_candidat) REFERENCES Candidat(id) ON DELETE CASCADE
);

CREATE TABLE poste (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255)
);

CREATE TABLE Annonce (
    id SERIAL PRIMARY KEY,
    role VARCHAR(150) NOT NULL,
    salaire NUMERIC(12,2),
    horaire_de_travail INT,
    lieu_de_poste VARCHAR(255),
    date_limite_postule TIMESTAMP,
    document_necessaire VARCHAR(255),
    id_poste INT NOT NULL REFERENCES poste(id)
);
-- ===================================
-- Tables d’association
-- ===================================

CREATE TABLE Annonce_formation (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL,
    id_formation INT NOT NULL,
    est_obligatoire BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_af_annonce FOREIGN KEY (id_annonce) REFERENCES Annonce(id) ON DELETE CASCADE,
    CONSTRAINT fk_af_formation FOREIGN KEY (id_formation) REFERENCES Formation(id) ON DELETE CASCADE
);

CREATE TABLE Annonce_competence (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL,
    id_competence INT NOT NULL,
    est_obligatoire BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_ac_annonce FOREIGN KEY (id_annonce) REFERENCES Annonce(id) ON DELETE CASCADE,
    CONSTRAINT fk_ac_competence FOREIGN KEY (id_competence) REFERENCES Competence(id) ON DELETE CASCADE
);

CREATE TABLE Annonce_langue (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL,
    id_langue INT NOT NULL,
    est_obligatoire BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_al_annonce FOREIGN KEY (id_annonce) REFERENCES Annonce(id) ON DELETE CASCADE,
    CONSTRAINT fk_al_langue FOREIGN KEY (id_langue) REFERENCES Langue(id) ON DELETE CASCADE
);

CREATE TABLE Annonce_loisir (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL,
    id_loisir INT NOT NULL,
    est_obligatoire BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_alo_annonce FOREIGN KEY (id_annonce) REFERENCES Annonce(id) ON DELETE CASCADE,
    CONSTRAINT fk_alo_loisir FOREIGN KEY (id_loisir) REFERENCES Loisir(id) ON DELETE CASCADE
);

CREATE TABLE Annonce_CV (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL,
    id_cv INT NOT NULL,
    CONSTRAINT fk_acv_annonce FOREIGN KEY (id_annonce) REFERENCES Annonce(id) ON DELETE CASCADE,
    CONSTRAINT fk_acv_cv FOREIGN KEY (id_cv) REFERENCES CV(id) ON DELETE CASCADE
);
-- ===================================
-- TABLES DE LIAISON POUR LES CV
-- ===================================

CREATE TABLE CV_formation (
    id SERIAL PRIMARY KEY,
    id_cv INT NOT NULL,
    id_formation INT NOT NULL,
    date_debut DATE,
    date_fin DATE,
    etablissement VARCHAR(255),
    CONSTRAINT fk_cv_formation_cv FOREIGN KEY (id_cv) REFERENCES CV(id) ON DELETE CASCADE,
    CONSTRAINT fk_cv_formation_formation FOREIGN KEY (id_formation) REFERENCES Formation(id) ON DELETE CASCADE
);

CREATE TABLE CV_competence (
    id SERIAL PRIMARY KEY,
    id_cv INT NOT NULL,
    id_competence INT NOT NULL,
    niveau VARCHAR(50), -- exemple: débutant, intermédiaire, expert
    CONSTRAINT fk_cv_competence_cv FOREIGN KEY (id_cv) REFERENCES CV(id) ON DELETE CASCADE,
    CONSTRAINT fk_cv_competence_competence FOREIGN KEY (id_competence) REFERENCES Competence(id) ON DELETE CASCADE
);

CREATE TABLE CV_langue (
    id SERIAL PRIMARY KEY,
    id_cv INT NOT NULL,
    id_langue INT NOT NULL,
    niveau VARCHAR(50), -- exemple: basique, courant, bilingue
    CONSTRAINT fk_cv_langue_cv FOREIGN KEY (id_cv) REFERENCES CV(id) ON DELETE CASCADE,
    CONSTRAINT fk_cv_langue_langue FOREIGN KEY (id_langue) REFERENCES Langue(id) ON DELETE CASCADE
);

CREATE TABLE CV_loisir (
    id SERIAL PRIMARY KEY,
    id_cv INT NOT NULL,
    id_loisir INT NOT NULL,
    CONSTRAINT fk_cv_loisir_cv FOREIGN KEY (id_cv) REFERENCES CV(id) ON DELETE CASCADE,
    CONSTRAINT fk_cv_loisir_loisir FOREIGN KEY (id_loisir) REFERENCES Loisir(id) ON DELETE CASCADE
);

-- ===================================
-- TABLES POUR LES TESTS ET QUESTIONS
-- ===================================

CREATE TABLE Question (
    id SERIAL PRIMARY KEY,
    question VARCHAR(255),
    point INT  
);

CREATE TABLE Reponse (
    id SERIAL PRIMARY KEY, 
    reponse VARCHAR(255)
);

CREATE TABLE Question_reponse (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL REFERENCES question(id),
    id_reponse INT NOT NULL REFERENCES reponse(id)
);

CREATE TABLE Correct_reponse (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL REFERENCES question(id),
    id_reponse INT NOT NULL REFERENCES reponse(id)
);

CREATE TABLE Test (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255)
);

CREATE TABLE Test_poste (
    id SERIAL PRIMARY KEY,
    id_test INT NOT NULL REFERENCES test(id),
    id_poste INT NOT NULL REFERENCES blog_poste(id)
);

CREATE TABLE Test_question (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL REFERENCES question(id),
    id_test INT NOT NULL REFERENCES test(id)
);

CREATE TABLE Score_question (
    id SERIAL PRIMARY KEY,
    note NUMERIC(12,2),
    id_question INT NOT NULL REFERENCES question(id),
    id_test INT NOT NULL REFERENCES test(id),
    id_candidat INT NOT NULL REFERENCES blog_candidat(id),
    id_annonce INT NOT NULL REFERENCES blog_annonce(id)
);

CREATE TABLE Score_entretien (
    id SERIAL PRIMARY KEY,
    note NUMERIC(12,2),
    id_annonce INT NOT NULL REFERENCES blog_annonce(id),
    id_candidat INT NOT NULL REFERENCES blog_candidat(id)
);

CREATE TABLE planning_entretien (
    id SERIAL PRIMARY KEY,
    date_entretien DATE,
    id_candidat INT NOT NULL REFERENCES blog_candidat(id),
    id_annonce INT NOT NULL REFERENCES blog_annonce(id)
);

CREATE TABLE score_total (
    id SERIAL PRIMARY KEY,
    id_candidat INT NOT NULL REFERENCES blog_candidat(id),
    id_annonce INT NOT NULL REFERENCES blog_annonce(id),
    note INT
);


--  CREATE TABLE annonce_status (
--     id_annonce SERIAL PRIMARY KEY,
--     status BOOLEAN
-- );