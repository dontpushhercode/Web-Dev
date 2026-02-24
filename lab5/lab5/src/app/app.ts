import { Component } from '@angular/core';
import { ProductList } from './components/product-list/product-list';
import { ShopPage } from './pages/shop-page/shop-page';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ShopPage],
  template: `<app-shop-page></app-shop-page>`
})
export class App {}
