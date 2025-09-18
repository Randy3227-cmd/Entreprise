-- ===================================
-- Création des tables principales
-- ===================================

CREATE TABLE formation (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE competence (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE langue (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE loisir (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE candidat (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telephone VARCHAR(30),
    date_naissance DATE,
    adresse VARCHAR(255)
);

CREATE TABLE cv (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(150) NOT NULL,
    resume TEXT,
    date_creation DATE DEFAULT CURRENT_DATE,
    id_candidat INT NOT NULL REFERENCES candidat(id)
);

CREATE TABLE poste (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255)
);

CREATE TABLE annonce (
    id SERIAL PRIMARY KEY,
    role VARCHAR(150) NOT NULL,
    salaire NUMERIC(12,2),
    horaire_de_travail TIMESTAMP,
    lieu_de_poste VARCHAR(255),
    contact VARCHAR(255),
    date_limite_postule TIMESTAMP,
    document_necessaire VARCHAR(255),
    site_web VARCHAR(255),
    reseaux_sociaux VARCHAR(255),
    id_poste INT NOT NULL REFERENCES poste(id)
);

-- ===================================
-- Tables d’association
-- ===================================

CREATE TABLE annonce_formation (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL REFERENCES annonce(id),
    id_formation INT NOT NULL REFERENCES formation(id)
);

CREATE TABLE annonce_competence (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL REFERENCES annonce(id),
    id_competence INT NOT NULL REFERENCES competence(id),
    est_obligatoire BOOLEAN DEFAULT FALSE
);

CREATE TABLE annonce_langue (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL REFERENCES annonce(id),
    id_langue INT NOT NULL REFERENCES langue(id),
    est_obligatoire BOOLEAN DEFAULT FALSE
);

CREATE TABLE annonce_loisir (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL REFERENCES annonce(id),
    id_loisir INT NOT NULL REFERENCES loisir(id),
    est_obligatoire BOOLEAN DEFAULT FALSE
);

CREATE TABLE annonce_cv (
    id SERIAL PRIMARY KEY,
    id_annonce INT NOT NULL REFERENCES annonce(id),
    id_cv INT NOT NULL REFERENCES cv(id)
);

CREATE TABLE question (
    id SERIAL PRIMARY KEY,
    question VARCHAR(255),
    point INT  
);

CREATE TABLE reponse (
    id SERIAL PRIMARY KEY, 
    reponse VARCHAR(255)
);

CREATE TABLE question_reponse (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL REFERENCES question(id),
    id_reponse INT NOT NULL REFERENCES reponse(id)
);

CREATE TABLE correct_reponse (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL REFERENCES question(id),
    id_reponse INT NOT NULL REFERENCES reponse(id)
);

CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255)
);

CREATE TABLE test_question (
    id SERIAL PRIMARY KEY,
    id_question INT NOT NULL REFERENCES question(id),
    id_test INT NOT NULL REFERENCES test(id)
);

CREATE TABLE score_question (
    id SERIAL PRIMARY KEY,
    note NUMERIC(12,2),
    id_question INT NOT NULL REFERENCES question(id),
    id_test INT NOT NULL REFERENCES test(id),
    id_candidat INT NOT NULL REFERENCES candidat(id),
    id_annonce INT NOT NULL REFERENCES annonce(id)
);

CREATE TABLE score_entretien (
    id SERIAL PRIMARY KEY,
    note NUMERIC(12,2),
    id_annonce INT NOT NULL REFERENCES annonce(id),
    id_candidat INT NOT NULL REFERENCES candidat(id)
);