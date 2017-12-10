CREATE TABLE "Ave" (
  "id_ave" serial NOT NULL PRIMARY KEY, 
  "codigo" varchar(200) NOT NULL, 
  "especie" varchar(200) NOT NULL, 
  "synonim" varchar(200) NOT NULL, 
  "nombre" varchar(200) NOT NULL, 
  "morfometria" varchar(200) NOT NULL, 
  "ecologia" varchar(200) NOT NULL, 
  "comportamiento" varchar(200) NOT NULL, 
  "clase" varchar(200) NOT NULL,  
  "llamar" varchar(200) NOT NULL, 
  "uicn" varchar(200) NOT NULL,
  "endemismo" varchar(200) NOT NULL, 
  "observacion" varchar(200) NOT NULL,
  "migracion" varchar(200) NOT NULL,
  "ecosistema" varchar(200) NOT NULL
  );

CREATE TABLE "Autores" (
  "id_autor" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200) NOT NULL,
  "bibliografia" varchar(200) NOT NULL,
  "fecha" date NOT NULL,
  "year_of_collection" varchar(200) NOT NULL,
  "year_of_public" varchar(200) NOT NULL,
  "source" varchar(200) NOT NULL);

CREATE TABLE "Familia" (
  "id_familia" serial NOT NULL PRIMARY KEY,
  "nombre" varchar(200) NOT NULL,
  "orden" varchar(200) NOT NULL);
 
CREATE TABLE "Ubicacion" (
  "id_ubicacion" serial NOT NULL PRIMARY KEY,
	"cordinate" varchar(200) NOT NULL, 
	"altitudMax" varchar(200) NOT NULL,
	"altitudMin" varchar(200) NOT NULL,
	"utmwgs" varchar(200) NOT NULL,
	"longitudY" varchar(200) NOT NULL,
	"latitudX" varchar(200) NOT NULL);
  
CREATE TABLE "Localidad" (
  "id_localidad" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200) NOT NULL,
  "toponim" varchar(200) NOT NULL,
  "pais" varchar(200) NOT NULL,
  "provincia" varchar(200) NOT NULL);
  
ALTER TABLE "Ave" ADD COLUMN "id_autor_id" integer NOT NULL;
ALTER TABLE "Ave" ALTER COLUMN "id_autor_id" DROP DEFAULT;
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
ALTER TABLE "Ubicacion" ADD COLUMN "id_localidad_id" integer NOT NULL;
ALTER TABLE "Ubicacion" ALTER COLUMN "id_localidad_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_familia" FOREIGN KEY ("id_familia_id") REFERENCES "Familia" ("id_familia") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_autor" FOREIGN KEY ("id_autor_id") REFERENCES "Autores" ("id_autor") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_ubicacion" FOREIGN KEY ("id_ubicacion_id") REFERENCES "Ubicacion" ("id_ubicacion") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ubicacion" ADD CONSTRAINT "FK_ubicacion_localidad" FOREIGN KEY ("id_localidad_id") REFERENCES "Localidad" ("id_localidad") DEFERRABLE INITIALLY DEFERRED;


