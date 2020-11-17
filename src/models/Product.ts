import { Column, CreateDateColumn, Entity, ManyToOne, PrimaryGeneratedColumn, Unique, UpdateDateColumn } from 'typeorm';
import { Max, MaxLength, MinLength } from 'class-validator';
import Brand from './Brand';

@Entity()
export default class Product {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    // @Column()
    // code: number;

    @Column()
    @MaxLength(100)
    @MinLength(3)
    name: string;

    @Column()
    @MaxLength(300)
    description: string;

    // @Column()
    // @MaxLength(300)
    // image: string;

    @Column()
    @MaxLength(3)
    unity: string;

    @Column()
    @Max(99999)
    quantity: number;

    @Column()
    @Max(99999)
    quantityMinimun: number;

    @Column({ type: "decimal" })
    sellPrice: number;

    @Column({ type: "decimal" })
    buyPrice: number;

    // @Column()
    // percentage: number;

    // @Column()
    // weight: number;

    @Column()
    featured: boolean;

    @ManyToOne(type => Brand, product => Product, { eager: true })
    brands: Brand;

    @CreateDateColumn({ name: 'created_At' })
    createdAt: Date;

    @UpdateDateColumn({ name: 'updated_At' })
    updatedAt: Date;

}