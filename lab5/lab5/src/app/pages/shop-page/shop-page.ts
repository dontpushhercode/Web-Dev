import { Component } from '@angular/core';
import { Header } from '../../components/header/header';
import { ProductList } from '../../components/product-list/product-list';
import { SidebarFilters } from '../../components/sidebar-filters/sidebar-filters';
import { SearchBar } from '../../components/search-bar/search-bar';
import { CategoriesMenu } from '../../components/categories-menu/categories-menu';
import { Favorites } from '../../components/favorites/favorites';
import { PRODUCTS } from '../../data/products';
import { Product } from '../../models/product';

@Component({
  selector: 'app-shop-page',
  standalone: true,
  imports: [Header, ProductList, SidebarFilters, SearchBar, CategoriesMenu, Favorites],
  templateUrl: './shop-page.html',
})
export class ShopPage {
  allProducts: Product[] = PRODUCTS;

  searchText = '';
  selectedCategory = 0;
  
  onSearch(text: string){
    this.searchText = text;
  }

  onCategoryChange(id: number) {
    this.selectedCategory = id;
  }

  removeProduct(productToRemove: Product) {
  this.allProducts = this.allProducts.filter(
    product => product !== productToRemove
  );
}
}