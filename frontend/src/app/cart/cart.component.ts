import { Component, OnInit } from '@angular/core';
import { CartService } from '../shared/service/cart.service';
import { Phone } from '../shared/module/phone.module';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  cartItems: Phone[]
  total_price = 0
  constructor(private cartService: CartService) { }

  ngOnInit(): void {
    this.getItemsInCart()
  }

  getItemsInCart() {
    this.cartItems = this.cartService.getCartItems()
    this.cartItems.forEach(item => {
      this.total_price += item.price * item.quantity
    });
  }

  show() {
    console.log(this.cartItems)
    console.log("hei")

  }
}
