import { Injectable } from '@angular/core';

import { HttpClient,HttpHeaders,HttpErrorResponse, HttpInterceptor,HttpRequest,HttpHandler,HttpEvent } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';

import { Observable,throwError } from 'rxjs';
import { tap, shareReplay } from 'rxjs/operators';

import * as jwtDecode from 'jwt-decode';
import * as moment from 'moment';

import { environment } from 'src/environments/environment';
import { User } from '../user';
import { catchError,map } from 'rxjs/operators';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})

export class AuthService {

  endpoint: string = 'https://taliban-trackerapp.herokuapp.com/auth/';
  headers = new HttpHeaders().set('Content-Type','application/json');
  currentUser = {};
  // getUserProfile:any;

  constructor(private http: HttpClient,public router: Router) { }

  signUp(user:User):Observable<any>{
    let api = `${this.endpoint}register/`;
    return this.http.post(api,user).pipe(catchError(this.handleError))
  }

  //sign in
  signIn(user: User){
    return this.http.post<any>(`${this.endpoint}token/`,user).subscribe((res: any)=>{
      localStorage.setItem('access',res.access)
      // this.getUserProfile(res._id).subscribe((res:any)=>{
      //   this.currentUser = res;
        this.router.navigate(['home']);
      // })
    })
  }
  getToken(){
    return localStorage.getItem('access');
  }

  get isLoggedIn(): boolean{
    let authToken = localStorage.getItem('access');
    return (authToken !== null)? true : false;
  }

  doLogout(){
    let removeToken = localStorage.removeItem('access');
    if (removeToken == null){
      this.router.navigate(['login'])

    }
  }

  //user profile
  getUserProfile(id:any): Observable<any> {
    let api = `${this.endpoint}profile/${id}`;
    return this.http.get(api, { headers: this.headers })
      // map((res: Response)=>{
      //   return res || {}
      // }),
      // catchError(this.handleError)
    // )

  }

  //Error
  handleError(error: HttpErrorResponse){
    let msg = '';
    if (error.error instanceof ErrorEvent){
      //client-side error
      msg = error.error.message;

    }else{
      //sever-side error
      msg  = `Error Code: ${error.status}\nMessage: ${error.message}`;

    }
    return throwError(msg);

  }

}
