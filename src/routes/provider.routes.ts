import { validate } from 'class-validator';
import { response, Router } from 'express';
import { getConnection, getRepository } from 'typeorm';
import Provider from '../models/Provider';

const providerRouter = Router();

providerRouter.get('/', async (request, response) => {
    response.json(await getRepository(Provider).find({ cache: { id: 'listProvider', milliseconds: 10000 } }))
})

providerRouter.post('/', async (request, response) => {
    try {
        const repo = getRepository(Provider);
        const provider = repo.create(request.body);
        const errors = await validate(provider);
        if (errors.length == 0) {
            const res = await repo.save(provider);
            await getConnection().queryResultCache?.remove(['listProvider']);
            return response.status(201).json(res);
        }
        return response.status(400).json(errors)
    } catch (err) {
        console.log('err.message >> ', err.message)
        return response.status(400).send()
    }
})

export default providerRouter;