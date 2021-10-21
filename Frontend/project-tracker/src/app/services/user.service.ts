import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class UserService {

  private httpOptions: any;

  public token?: string;

  public token_expires?: Date;

  public username?: string;

  public errors: any=[];
  // updateData: any;

  constructor(private http: HttpClient) { 
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

  // public login(user:any){
  //   this.http.post('/token/',JSON.stringify(user),this.httpOptions).subscribe(
  //    data =>{
  //     this.updateData(data['token']);
  //    },
  //    err => {
  //      this.errors  = err['error'];
  //    } 
  //   );
  // }
  // public refreshToken() {
  //   this.http.post('/api-token-refresh/', JSON.stringify({token: this.token}), this.httpOptions).subscribe(
  //     data => {
  //       this.updateData(data['token']);
  //     },
  //     err => {
  //       this.errors = err['error'];
  //     }
  //   );
  // }
  // public logout() {
  //   this.token = null;
  //   this.token_expires = null;
  //   this.username = null;
  // }
  private updateData(token:any) {
    this.token = token;
    this.errors = [];
 
    // decode the token to read the username and expiration timestamp
    // const token_parts = this.token.split(/\./);
    // const token_decoded = JSON.parse(window.atob(token_parts[1]));
    // this.token_expires = new Date(token_decoded.exp * 1000);
    // this.username = token_decoded.username;
  }
}
