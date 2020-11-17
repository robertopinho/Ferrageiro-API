import { Router } from 'express';
import Brand from '../models/Brand';
import { validate } from 'class-validator';
import { getConnection, getRepository } from 'typeorm';

const brandRouter = Router();

brandRouter.post('/', async (request, response) => {
    try {
        const repo = getRepository(Brand);
        const brand = repo.create(request.body);
        const errors = await validate(brand);
        if (errors.length == 0) {
            const res = await repo.save(brand);
            await getConnection().queryResultCache?.remove(['listBrand']);
            return response.status(201).json(res);
        }
        return response.status(400).json(errors)
    } catch (err) {
        console.log('err.message >> ', err.message)
        return response.status(400).send()
    }
})

brandRouter.get('/', async (request, response) => {
    response.json(await getRepository(Brand).find({ cache: { id: 'listBrand', milliseconds: 10000 } }))
})


export default brandRouter;