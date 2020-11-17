import { validate } from 'class-validator';
import { Router } from 'express';
import { getConnection, getRepository } from 'typeorm';
import Category from '../models/Category';

const categoryRouter = Router();

categoryRouter.get('/', async (request, response) => {
    response.json(await getRepository(Category).find({ cache: { id: 'listCategory', milliseconds: 10000 } }));
})

categoryRouter.post('/', async (request, response) => {
    try {
        const repo = getRepository(Category);
        const category = repo.create(request.body);
        const errors = await validate(category);
        if (errors.length == 0) {
            const res = await repo.save(category);
            await getConnection().queryResultCache?.remove(['listCategory']);
            return response.status(201).json(res);
        }
        return response.status(400).json(errors);
    } catch (err) {
        console.log('err.message >> ', err.message);
        return response.status(400).send();
    }
})
export default categoryRouter;