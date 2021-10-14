import { Injectable } from '@angular/core';
import { HttpClient, HttpInterceptor,HttpRequest,HttpHandler,HttpEvent } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';

import { Observable } from 'rxjs';
import { tap, shareReplay } from 'rxjs/operators';

import * as jwtDecode from 'jwt-decode';
import * as moment from 'moment';

import { environment } from 'src/environments/environment';



@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiRoot = 'http://localhost:8000/auth/';

  constructor(private http: HttpClient) { }

  // private setSession(authResult:any){
  //   const token = authResult.token;
  //   const payload = <JWTPayload> jwtDecode(token);
  // }
}
