import { validate } from 'class-validator';
import { response, Router } from 'express';
import { getConnection, getRepository } from 'typeorm';
import Product from '../models/Product';

const productRouter = Router();

productRouter.get('/', async (request, response) => {
    response.json(await getRepository(Product).find({ cache: { id: 'listProduct', milliseconds: 10000 } }))
})

productRouter.post('/', async (request, response) => {
    try {
        const repo = getRepository(Product);
        const product = repo.create(request.body);
        const errors = await validate(product);
        if (errors.length == 0) {
            const res = await repo.save(product);
            await getConnection().queryResultCache?.remove(['listProduct']);
            return response.status(201).json(res);
        }
        return response.status(400).json(errors)
    } catch (err) {
        console.log('err.message >> ', err.message)
        return response.status(400).send()
    }
})

export default productRouter;