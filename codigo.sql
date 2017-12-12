CREATE TABLE "Ave" (
  "id_ave" serial NOT NULL PRIMARY KEY, 
  "codigo" varchar(200), 
  "especie" varchar(200), 
  "synonim" varchar(200), 
  "nombre" varchar(200), 
  "morfometria" varchar(200), 
  "ecologia" varchar(200), 
  "comportamiento" varchar(200), 
  "clase" varchar(200),  
  "llamar" varchar(200), 
  "uicn" varchar(200),
  "endemismo" varchar(200), 
  "observacion" varchar(200),
  "migracion" varchar(200),
  "ecosistema" varchar(200)
  );

CREATE TABLE "Autores" (
  "id_autor" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200),
  "bibliografia" varchar(200),
  "fecha" varchar(200),
  "year_of_collection" varchar(200),
  "year_of_public" varchar(200),
  "source" varchar(200));

CREATE TABLE "Familia" (
  "id_familia" serial NOT NULL PRIMARY KEY,
  "nombre" varchar(200),
  "orden" varchar(200));
 
CREATE TABLE "Ubicacion" (
  "id_ubicacion" serial NOT NULL PRIMARY KEY,
	"cordinate" varchar(200), 
	"altitudMax" varchar(200),
	"altitudMin" varchar(200),
	"utmwgs" varchar(200),
	"longitudY" varchar(200),
	"latitudX" varchar(200));
  
CREATE TABLE "Localidad" (
  "id_localidad" serial NOT NULL PRIMARY KEY, 
  "nombre" varchar(200),
  "toponim" varchar(200),
  "pais" varchar(200),
  "provincia" varchar(200));
  
ALTER TABLE "Ave" ADD COLUMN "id_autor_id" integer NOT NULL;
ALTER TABLE "Ave" ALTER COLUMN "id_autor_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_bibliografia_id" integer NOT NULL;
ALTER TABLE "Ave" ALTER COLUMN "id_bibliografia_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_familia_id" integer NOT NULL UNIQUE;
ALTER TABLE "Ave" ALTER COLUMN "id_familia_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD COLUMN "id_ubicacion_id" integer NOT NULL;
ALTER TABLE "Ave" ALTER COLUMN "id_ubicacion_id" DROP DEFAULT;
ALTER TABLE "Ubicacion" ADD COLUMN "id_localidad_id" integer NOT NULL;
ALTER TABLE "Ubicacion" ALTER COLUMN "id_localidad_id" DROP DEFAULT;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_familia" FOREIGN KEY ("id_familia_id") REFERENCES "Familia" ("id_familia") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_autor" FOREIGN KEY ("id_autor_id") REFERENCES "Autores" ("id_autor") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ave" ADD CONSTRAINT "FK_ave_ubicacion" FOREIGN KEY ("id_ubicacion_id") REFERENCES "Ubicacion" ("id_ubicacion") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Ubicacion" ADD CONSTRAINT "FK_ubicacion_localidad" FOREIGN KEY ("id_localidad_id") REFERENCES "Localidad" ("id_localidad") DEFERRABLE INITIALLY DEFERRED;


