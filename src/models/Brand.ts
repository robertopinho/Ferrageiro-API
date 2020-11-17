import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from 'typeorm';
import Product from './Product';

@Entity()
export default class Brand {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column()
    name: string;
    
    @OneToMany(type => Product, brands => Brand)
    product: Product[];

}