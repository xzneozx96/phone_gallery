import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Phone } from '../module/phone.module';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  PhoneList: Phone[] = []
  constructor(private httpClient: HttpClient) { }

  addItemsToCart(item: Phone, quantity: number) {
    const phoneWithQuantity = new Phone(
      item.name,
      item.quantity = quantity,
      item.linkproduct,
      item.category,
      item.imageURL,
      item.price,
      item.description
    )
    this.PhoneList.push(phoneWithQuantity)
  }

  getCartItems(): Phone[] {
    return this.PhoneList
  }

  clearCart() {
    this.PhoneList = []
  }

  showCartItems() {
    console.log(this.PhoneList)
  }
}
