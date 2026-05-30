create database edusync02;

use edusync02;
CREATE TABLE gestao(
	gestao_id INT AUTO_INCREMENT PRIMARY KEY,
	gestao_nome VARCHAR(150) NOT NULL,
    gestao_usu VARCHAR(150) NOT NULL,
    gestao_senha VARCHAR(150) NOT NULL,
	gestao_email VARCHAR(150) NOT NULL,
	gestao_cargo VARCHAR(150) NOT NULL,
	gestao_status VARCHAR(150) NOT NULL
    );

INSERT INTO gestao(gestao_id,gestao_nome,gestao_usu,gestao_senha,gestao_email,gestao_cargo,gestao_status)VALUES
	(1,'Marcos Rocha','MarcosRo','marcos2022','marcos.coord@escola.com', 'Coordenador', 'Ativo'),
    (2,'Beatriz Lima','BeatrizLi','beatriz2025','beatriz.rh@escola.com', 'Diretora', 'Ativo'),
    (3,'Carlos Melo','CarlosMe','carlos1990','carlos.vice@escola.com', 'Vice-Diretor', 'Inativo');

    
CREATE TABLE atribuicao(
		atribuicao_id INT AUTO_INCREMENT PRIMARY KEY,
        atribuicao_nome VARCHAR(150) NOT NULL
  );
  
INSERT INTO atribuicao(atribuicao_id, atribuicao_nome) VALUES
		(1,'Português'),
        (2,'História'),
        (3,'Matemática'),
		(4,'Literatura'),
		(5,'Física'),
		(6,'Sociologia'),
        (7,'Filosofia'),
        (8,'Geografia'),
        (9,'Biologia'),
        (10,'Química'),
        (11,'Inglês'),
        (12,'Espanhol'),
        (13,'Geopolítica');
        

CREATE TABLE disciplina(
        disciplina_id INT AUTO_INCREMENT PRIMARY KEY,
        disciplina_nome VARCHAR(150) NOT NULL,
        carga_horaria INT
    );
    
INSERT INTO disciplina( disciplina_id, disciplina_nome, carga_horaria)VALUES
	(1,'Estudos Avançados de Língua Portuguesa', 32),
    (2,'Fundamentos de História Geral', 24),
    (3,'Tópicos de Matemática Aplicada', 32),
    (4,'Análise Literária e Produção Textual',16),
    (5,'Princípios de Física Experimental',24),
    (6,'Teorias Sociológicas Contemporâneas',16),
    (7,'Introdução ao Pensamento Filosófico',16),
    (8,'Estudos Geográficos e Ambientais',16),
    (9,'Biologia Geral e Aplicada',24),
    (10,'Fundamentos de Química Experimental',24),
    (11,'Comunicação e Estruturas da Língua Inglesa',16);
    
CREATE TABLE professor(
        professor_id INT AUTO_INCREMENT PRIMARY KEY ,
        professor_nome VARCHAR(150) NOT NULL,
        professor_usu VARCHAR(150) NOT NULL,
        professor_senha VARCHAR(150) NOT NULL,
        professor_email VARCHAR(150) NOT NULL
    );
    
INSERT INTO professor(professor_id,professor_nome,professor_usu,professor_senha,professor_email)VALUES
	(1,'Fernanda Oliveira','FernandaOli','fernanda2007','fernanda2007@gmail.com'),
	(2,'Roberto Alencar','RobertoAl','roberto2009','roberto2009@gmail.com'),
	(3,'Juliana Costa','JulianaCo','juliana2020','juliana2020@gmail.com'),    
	(4,'Lorenzo Silva','LorenzoSi','lorenzo2018','lorenzo2018@gmail.com'),
    (5,'Leonardo Souza','LeonardoSo','leonardo2008','leonardo2008@gmail.com'),
    (6,'Luca Nascimento','LucaNa','luca2007','luca2007@gmail.com'),
    (7,'Verônica Brown','VerônicaBr','veronica1998','veronica1998@gmail.com'),
    (8,'Darti Miller','DartiMi','darti1979','dartimi1979@gmail.com');
    
CREATE TABLE turma(
        turma_id INT AUTO_INCREMENT PRIMARY KEY,
        turma_periodo VARCHAR(150),
        turma_sala VARCHAR(150),
        turma_status VARCHAR(150),
        disciplina_iid INT,
        FOREIGN KEY (disciplina_iid) REFERENCES disciplina(disciplina_id)
    );

INSERT INTO turma( turma_id, turma_periodo, turma_sala, turma_status,disciplina_iid) VALUES
	(1,'Manhã','Sala 10','Ativo',1),
    (2,'Manhã','Sala 11','Ativo',2),
    (3,'Manhã','Sala 12','Ativo',3),
    (4,'Manhã','Sala 13','Ativo',4),
    (5,'Tarde','Sala 14','Ativo',5),
    (6,'Tarde','Sala 15','Ativo',6),
    (7,'Tarde','Sala 16','Ativo',7),
    (8,'Tarde','Sala 17','Ativo',8),
    (9,'Noite','Sala 18','Ativo',9),
    (10,'Noite','Sala 19','Ativo',10),
    (11,'Noite','Sala 20','Ativo',11);

CREATE TABLE professor_turma (
    professor_iid INT,
    turma_iid INT,
    PRIMARY KEY (professor_iid, turma_iid),
    FOREIGN KEY (professor_iid) REFERENCES professor(professor_id) on delete cascade,
    FOREIGN KEY (turma_iid) REFERENCES turma(turma_id)
);

insert into professor_turma(professor_iid,turma_iid)values
	(1,1),
	(1,4),
    (2,3),
    (2,5),
    (3,2),
    (3,8),
	(4,9),
    (5,10),
    (6,11),
    (8,6),
    (8,7);
    
CREATE TABLE professor_atribuicao (
    professor_iid INT,
    atribuicao_iid INT,
    PRIMARY KEY (professor_iid, atribuicao_iid),
    FOREIGN KEY (professor_iid) REFERENCES professor(professor_id) on delete cascade,
    FOREIGN KEY (atribuicao_iid) REFERENCES atribuicao(atribuicao_id)
);

insert into professor_atribuicao(professor_iid,atribuicao_iid) values
		(1,1),
        (1,4),
        (2,3),
        (2,5),
		(3,2),
        (3,8),
		(4,9),
        (5,10),
        (6,12),
        (7,13),
        (8,6),
        (8,7);
        
CREATE TABLE contrato(
        contrato_id INT AUTO_INCREMENT PRIMARY KEY,
        contrato_data_inicio DATE,
        contrato_data_fim DATE,
        contrato_tipo VARCHAR(150),
        contrato_status VARCHAR(150),
        professor_iid INT,
        gestao_iid INT,
        FOREIGN KEY (professor_iid) REFERENCES professor(professor_id) on delete cascade,
        FOREIGN KEY (gestao_iid) REFERENCES gestao(gestao_id)
    );
        
SELECT professor_nome, turma_sala
FROM professor_turma
inner JOIN professor ON professor_iid = professor_id
inner JOIN turma ON turma_iid = turma_id
group by professor_nome, turma_sala;

CREATE TABLE aluno(
        aluno_ra INT AUTO_INCREMENT PRIMARY KEY,
        aluno_nome VARCHAR(150) NOT NULL,
        aluno_usu VARCHAR(150) NOT NULL,
        aluno_senha VARCHAR(150) NOT NULL,
        data_nascimento DATE,
        aluno_email VARCHAR(150) NOT NULL,
        aluno_telefone CHAR(11),
        aluno_status VARCHAR(150),
        turma_iid INT,
        FOREIGN KEY (turma_iid) REFERENCES turma(turma_id)
    );

 INSERT INTO aluno(aluno_ra ,aluno_nome,aluno_usu,aluno_senha,data_nascimento,aluno_email,aluno_telefone,aluno_status,turma_iid)VALUES
	(2026002, 'Mariana Gomes','MariaGo','maria2007','2007-11-02', 'mari.gomes@email.com' , '11977776666', 'Ativo', 3),
    (2026003, 'Enzo Ferrari','EnzoFe','enzo2009','2009-01-25', 'enzo.ferrari@email.com', '11955554444', 'Ativo' , 2),
    (2026004, 'Sophia Luz','SophiaLu','sophia2008','2008-08-12', 'sophia.luz@email.com', '11933332222', 'Ativo', 1 ),
	(2026005, 'Elena Georgi', 'ElenaGe', 'elena2010', '2010-05-23', 'elena.georgia@gmail.com', '11988881111', 'Ativo',4),
    (2026006, 'Rafael Rocha', 'RafaelRo', 'rafael2007','2007-12-14', 'rafael.rocha@gmail.com', '11974652973', 'Ativo',9),
    (2026007, 'Peter Santos', 'PeterSa', 'peter2008','2008-08-02', 'peter.santos@gmail.com', '11973826241', 'Ativo',6),
    (2026008, 'Fabiola Hernandes','FabiolaHe', 'fabiola2009', '2009-01-27', 'fabiola.hernandes@gmail.com', '11963501223', 'Ativo',7),
    (2026009, 'Alicia Meireles','AliciaMe', 'alicia2010','2010-09-17', 'alicia.meireles@gmail.com', '11903455623', 'Ativo',11),
    (2026010, 'Pietra Paixão','PietraPa', 'pietra2007','2007-02-06', 'pietra.paixao@gmail.com', '11976516250', 'Ativo',5),
    (2026011, 'Luke Barla','LukeBa', 'luke2009','2009-08-05', 'luke.barla@gmail.com', '11924690991', 'Ativo',8),
    (2026012, 'Jhon Fill','JhonFi', 'jhon2008','2008-01-16', 'jhon.fill@gmail.com', '11923782091', 'Ativo',10);
    
CREATE TABLE matricula(
        matricula_id INT AUTO_INCREMENT PRIMARY KEY ,
        matricula_data DATE,
        matricula_status VARCHAR(150),
        matricula_ra INT,
        gestao_id INT,
        FOREIGN KEY ( matricula_ra) REFERENCES aluno(aluno_ra),
        FOREIGN KEY (gestao_id) REFERENCES gestao(gestao_id)
    );
    
CREATE TABLE nota(
        nota_id INT AUTO_INCREMENT PRIMARY KEY,
        nota_valor DECIMAL(4,2),
        nota_frequencia INT,
        nota_rra INT,
        disciplina_iid INT,
        professor_iid INT,
        FOREIGN KEY (nota_rra) REFERENCES aluno(aluno_ra),
        FOREIGN KEY (disciplina_iid) REFERENCES disciplina(disciplina_id),
        FOREIGN KEY (professor_iid) REFERENCES professor(professor_id)
    );

INSERT INTO nota(nota_valor,nota_frequencia,nota_rra,disciplina_iid,professor_iid)VALUES
	(7.0, 85, 2026002, 3, 1),
    (6.5, 90, 2026003, 2, 2),
    (10.0, 100, 2026004 , 1 , 3),
    (9.0,80,2026005,4,1),
    (6.0,70,2026006,9,4),
    (10.0,100,2026007,6,8),
    (8.5,85,2026008,7,8),
    (5.5,60,2026009,11,6),
    (3.0,40,2026010,5,2),
    (9.0,90,2026011,8,3),
    (10.0,100,2026012,10,5);

CREATE TABLE boletim(
        boletim_id INT AUTO_INCREMENT PRIMARY KEY,
		boletim_ano INT,
        boletim_nota int,
		boletim_ra INT,
        FOREIGN KEY (boletim_nota) REFERENCES nota(nota_id),
        FOREIGN KEY (boletim_ra) REFERENCES aluno(aluno_ra)
    );
