import {MigrationInterface, QueryRunner} from "typeorm";

export class NewDatabase1605615953549 implements MigrationInterface {
    name = 'NewDatabase1605615953549'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TABLE "product" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "name" character varying NOT NULL, "description" character varying NOT NULL, "unity" character varying NOT NULL, "quantity" integer NOT NULL, "quantityMinimun" integer NOT NULL, "sellPrice" numeric NOT NULL, "buyPrice" numeric NOT NULL, "featured" boolean NOT NULL, "created_At" TIMESTAMP NOT NULL DEFAULT now(), "updated_At" TIMESTAMP NOT NULL DEFAULT now(), "brandsId" uuid, CONSTRAINT "PK_bebc9158e480b949565b4dc7a82" PRIMARY KEY ("id"))`);
        await queryRunner.query(`CREATE TABLE "brand" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "name" character varying NOT NULL, CONSTRAINT "PK_a5d20765ddd942eb5de4eee2d7f" PRIMARY KEY ("id"))`);
        await queryRunner.query(`CREATE TABLE "category" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "name" character varying NOT NULL, CONSTRAINT "UQ_23c05c292c439d77b0de816b500" UNIQUE ("name"), CONSTRAINT "PK_9c4e4a89e3674fc9f382d733f03" PRIMARY KEY ("id"))`);
        await queryRunner.query(`CREATE TABLE "provider" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "name" character varying NOT NULL, "cnpj" character varying(14) NOT NULL, "phone" character varying NOT NULL, "email" character varying NOT NULL, CONSTRAINT "UQ_8b153257b787a5b1ac08d58a4f1" UNIQUE ("cnpj"), CONSTRAINT "PK_6ab2f66d8987bf1bfdd6136a2d5" PRIMARY KEY ("id"))`);
        await queryRunner.query(`CREATE TABLE "category_products_product" ("categoryId" uuid NOT NULL, "productId" uuid NOT NULL, CONSTRAINT "PK_0b4e34a45516284987c6dbe91cd" PRIMARY KEY ("categoryId", "productId"))`);
        await queryRunner.query(`CREATE INDEX "IDX_90d521137ff8c3e927187bcd27" ON "category_products_product" ("categoryId") `);
        await queryRunner.query(`CREATE INDEX "IDX_ee240b247f9f23e5d35854c186" ON "category_products_product" ("productId") `);
        await queryRunner.query(`CREATE TABLE "provider_products_product" ("providerId" uuid NOT NULL, "productId" uuid NOT NULL, CONSTRAINT "PK_591107205ade43fe9a6ac19264f" PRIMARY KEY ("providerId", "productId"))`);
        await queryRunner.query(`CREATE INDEX "IDX_e9ea57eb5e70a99ff4e5a617cf" ON "provider_products_product" ("providerId") `);
        await queryRunner.query(`CREATE INDEX "IDX_90e331f323b6ae91b773b8c9b3" ON "provider_products_product" ("productId") `);
        await queryRunner.query(`ALTER TABLE "product" ADD CONSTRAINT "FK_9eb6eeb7eb88ca8f4b4f7e35879" FOREIGN KEY ("brandsId") REFERENCES "brand"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "category_products_product" ADD CONSTRAINT "FK_90d521137ff8c3e927187bcd27d" FOREIGN KEY ("categoryId") REFERENCES "category"("id") ON DELETE CASCADE ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "category_products_product" ADD CONSTRAINT "FK_ee240b247f9f23e5d35854c186b" FOREIGN KEY ("productId") REFERENCES "product"("id") ON DELETE CASCADE ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "provider_products_product" ADD CONSTRAINT "FK_e9ea57eb5e70a99ff4e5a617cfc" FOREIGN KEY ("providerId") REFERENCES "provider"("id") ON DELETE CASCADE ON UPDATE NO ACTION`);
        await queryRunner.query(`ALTER TABLE "provider_products_product" ADD CONSTRAINT "FK_90e331f323b6ae91b773b8c9b39" FOREIGN KEY ("productId") REFERENCES "product"("id") ON DELETE CASCADE ON UPDATE NO ACTION`);
        await queryRunner.query(`CREATE TABLE "query-result-cache" ("id" SERIAL NOT NULL, "identifier" character varying, "time" bigint NOT NULL, "duration" integer NOT NULL, "query" text NOT NULL, "result" text NOT NULL, CONSTRAINT "PK_6a98f758d8bfd010e7e10ffd3d3" PRIMARY KEY ("id"))`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`DROP TABLE "query-result-cache"`);
        await queryRunner.query(`ALTER TABLE "provider_products_product" DROP CONSTRAINT "FK_90e331f323b6ae91b773b8c9b39"`);
        await queryRunner.query(`ALTER TABLE "provider_products_product" DROP CONSTRAINT "FK_e9ea57eb5e70a99ff4e5a617cfc"`);
        await queryRunner.query(`ALTER TABLE "category_products_product" DROP CONSTRAINT "FK_ee240b247f9f23e5d35854c186b"`);
        await queryRunner.query(`ALTER TABLE "category_products_product" DROP CONSTRAINT "FK_90d521137ff8c3e927187bcd27d"`);
        await queryRunner.query(`ALTER TABLE "product" DROP CONSTRAINT "FK_9eb6eeb7eb88ca8f4b4f7e35879"`);
        await queryRunner.query(`DROP INDEX "IDX_90e331f323b6ae91b773b8c9b3"`);
        await queryRunner.query(`DROP INDEX "IDX_e9ea57eb5e70a99ff4e5a617cf"`);
        await queryRunner.query(`DROP TABLE "provider_products_product"`);
        await queryRunner.query(`DROP INDEX "IDX_ee240b247f9f23e5d35854c186"`);
        await queryRunner.query(`DROP INDEX "IDX_90d521137ff8c3e927187bcd27"`);
        await queryRunner.query(`DROP TABLE "category_products_product"`);
        await queryRunner.query(`DROP TABLE "provider"`);
        await queryRunner.query(`DROP TABLE "category"`);
        await queryRunner.query(`DROP TABLE "brand"`);
        await queryRunner.query(`DROP TABLE "product"`);
    }

}
