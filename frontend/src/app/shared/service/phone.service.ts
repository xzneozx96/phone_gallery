import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { API_URL } from '../../env';
import { getLocaleDateFormat } from '@angular/common';
import { catchError, map } from 'rxjs/operators';
import { Observable, Subscription } from 'rxjs';
import { link } from 'fs';
import { Phone } from '../module/phone.module';

@Injectable({
  providedIn: 'root',
})
export class PhoneService {
  phones: any;
  linkproduct: string;
  phone_info: Subscription;
  phonesList: Phone[];

  url = `${API_URL}/phones`;
  single_phone_url = `${API_URL}/phones/phoneslist`;

  phone_detail: string;
  constructor(private httpClient: HttpClient) {}
  ngOnInit(): void {
    //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
    //Add 'implements OnInit' to the class.
  }
  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(
      err.message || 'Error: Unable to complete request.'
    );
  }

  getData(): Observable<any> {
    return this.httpClient.get(this.url).pipe(
      catchError((error) => {
        return Observable.throw('Something went wrong ;)');
      })
    );
  }

  getPhoneInfor(linkproduct) {
    this.phone_info = this.getData().subscribe((res) => {
      this.phonesList = res;
    }, console.error);

    const result = this.phonesList.find((phone) => phone.linkproduct === linkproduct)
    console.log(result)
  }
}
