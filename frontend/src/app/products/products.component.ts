import { Component, OnInit } from '@angular/core';
import { PhoneService } from '../shared/phone.service';
import { Phone } from '../shared/phone.module';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css'],
})
export class ProductsComponent implements OnInit {
  constructor(private phoneService: PhoneService) {}
  phone_infor: Subscription;
  phonesList: any;

  ngOnInit() {
    this.phone_infor = this.phoneService.getData().subscribe((res) => {
      this.phonesList = res;
      console.log(typeof(res))
    }, console.error);
  }

  ngOnDestroy(): void {
    this.phone_infor.unsubscribe();
  }
  getInfor() {
    console.log(this.phonesList.name)
  }
}
