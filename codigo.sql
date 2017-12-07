CREATE TABLE "Autor" (
  "id_autor" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200) NOT NULL);
  
CREATE TABLE "Ave" (
  "id" serial NOT NULL PRIMARY KEY, 
  "codigo" varchar(200) NOT NULL, 
  "especie" varchar(200) NOT NULL, 
  "synonim" varchar(200) NOT NULL, 
  "nombre" varchar(200) NOT NULL, 
  "morfometres" varchar(200) NOT NULL, 
  "ecology" varchar(200) NOT NULL, 
  "behaviour" varchar(200) NOT NULL, 
  "yearPublished" varchar(200) NOT NULL, 
  "yearCollection" varchar(200) NOT NULL, 
  "date" varchar(200) NOT NULL, 
  "call" varchar(200) NOT NULL, 
  "observacion" varchar(200) NOT NULL, 
  "id_autor_id" integer NOT NULL);
  
CREATE TABLE "Bibliografia" (
  "id_bibliografia" serial NOT NULL PRIMARY KEY, 
  "bibliografia" text NOT NULL);
  
CREATE TABLE "Endemismo" (
  "id_endemismo" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200) NOT NULL);
  
CREATE TABLE "Familia" (
  "id_familia" serial NOT NULL PRIMARY KEY,
  "nombre" varchar(200) NOT NULL,
  "orden" varchar(200) NOT NULL);
  
CREATE TABLE "Migracion" (
  "id_migracion" serial NOT NULL PRIMARY KEY,
  "nombre" varchar(200) NOT NULL);
 
CREATE TABLE "Ubicacion" (
  "id_ubicacion" serial NOT NULL PRIMARY KEY, 
	"pais" varchar(200) NOT NULL, 
	"provincia" varchar(200) NOT NULL,
	"localidad" varchar(200) NOT NULL,
	"toponim" varchar(200) NOT NULL,
	"longitud" varchar(200) NOT NULL,
	"latitud" varchar(200) NOT NULL,
	"gps" varchar(200) NOT NULL,
	"latitudMax" varchar(200) NOT NULL,
	"latitudMin" varchar(200) NOT NULL,
	"id_ave" varchar(200) NOT NULL);
  
CREATE TABLE "Uicn" (
  "id_familia" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200) NOT NULL);
  
ALTER TABLE "Ave" ADD COLUMN "id_bibliografia_id" integer NOT NULL;
ALTER TABLE "Ave" ALTER COLUMN "id_bibliografia_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_endemismo_id" integer NOT NULL UNIQUE;
ALTER TABLE "Ave" ALTER COLUMN "id_endemismo_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_familia_id" integer NOT NULL UNIQUE;
ALTER TABLE "Ave" ALTER COLUMN "id_familia_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_migracion_id" integer NOT NULL UNIQUE;
ALTER TABLE "Ave" ALTER COLUMN "id_migracion_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_ubicacion_id" integer NOT NULL;
ALTER TABLE "Ave" ALTER COLUMN "id_ubicacion_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_autor" FOREIGN KEY ("id_autor_id") REFERENCES "Autor" ("id_autor") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_bibliografia" FOREIGN KEY ("id_bibliografia_id") REFERENCES "Bibliografia" ("id_bibliografia") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_endemismo" FOREIGN KEY ("id_endemismo_id") REFERENCES "Endemismo" ("id_endemismo") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_familia" FOREIGN KEY ("id_familia_id") REFERENCES "Familia" ("id_familia") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_migracion" FOREIGN KEY ("id_migracion_id") REFERENCES "Migracion" ("id_migracion") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_ubicacion" FOREIGN KEY ("id_ubicacion_id") REFERENCES "Ubicacion" ("id_ubicacion") DEFERRABLE INITIALLY DEFERRED;
