import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { API_URL } from '../env';
import { getLocaleDateFormat } from '@angular/common';
import { catchError, map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { Phone } from './phone.module';
@Injectable({
  providedIn: 'root',
})
export class PhoneService {
  phones: any;
  url = `${API_URL}/phones`;

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
      // map((data: any) => data),
      catchError((error) => {
        return Observable.throw('Something went wrong ;)');
      })
    );
  }
}
