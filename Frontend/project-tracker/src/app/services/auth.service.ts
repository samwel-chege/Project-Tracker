import { Injectable } from '@angular/core';
import { HttpClient, HttpInterceptor,HttpRequest,HttpHandler,HttpEvent, HttpHeaders, HttpResponse } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';

import { Observable } from 'rxjs';
import { tap, shareReplay, map } from 'rxjs/operators';
import 'rxjs/add/operator/map';

import * as jwtDecode from 'jwt-decode';
import * as moment from 'moment';

import { environment } from 'src/environments/environment';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})

export class AuthService {

  api_url: string = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }

  login(email: string, password: string) {
    return this.http.post<any>(this.api_url + 'login',
      { email, password }, httpOptions).pipe(
        map(user => {
          if (user && user.tokens) {
            localStorage.setItem("currentUser", JSON.stringify(user));
          }
          return user;
        }
      )
    );
  }

  // register(user): Observable<any> {
  //   return this.http.post<any>(this.api_url + 'register', {
  //     username: user.username,
  //     email: user.email,
  //     password: user.password
  //   }, httpOptions);
  // }

  logout(){
    localStorage.removeitem('currentUser');
  }
}
