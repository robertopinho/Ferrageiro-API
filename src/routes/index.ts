import { Router } from 'express';
import brandRouter from './brand.routes';
import categoryRouter from './category.routes';
import productRouter from './product.routes'
import providerRouter from './provider.routes';

const routes = Router();
routes.use('/product', productRouter)
routes.use('/brand', brandRouter)
routes.use('/category', categoryRouter)
routes.use('/provider', providerRouter)
export default routes;