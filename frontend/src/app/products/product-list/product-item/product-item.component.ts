import { Component, OnInit } from '@angular/core';
import { PhoneService } from 'src/app/shared/service/phone.service';
import { CartService } from 'src/app/shared/service/cart.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  constructor(private phoneService: PhoneService, private cartService: CartService) { }


  phone_infor: Subscription;
  phonesList: any;
  len: number;
  ngOnInit() {
    this.phone_infor = this.phoneService.getData().subscribe((res) => {
      this.phonesList = res;
    }, console.error);
  }


  addItemToCart(name: string) {
    const item = this.phonesList.find((phone)=> phone.name === name);
    this.cartService.addItemsToCart(item,1)
    this.cartService.showCartItems()
  }

  getPhoneDetail(name: string) {
    this.phoneService.getPhoneInfor(name)
  }  
}
