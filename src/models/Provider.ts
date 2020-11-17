import { Length, MaxLength, MinLength } from "class-validator";
import { Column, Entity, JoinColumn, JoinTable, ManyToMany, PrimaryGeneratedColumn } from "typeorm";
import Product from "./Product";


@Entity()
export default class Provider {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column()
    name: string;

    @Column({unique: true, length: 14, nullable: false})
    cnpj: string;

    @Column()
    phone: string;

    @Column()
    email: string;

    @ManyToMany(type => Product)
    @JoinTable()
    products: Product;

}