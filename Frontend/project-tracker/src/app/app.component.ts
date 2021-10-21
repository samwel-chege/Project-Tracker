import { Component, OnInit } from '@angular/core';
import { ProjectService } from './services/project.service';
import { AuthService } from './services/auth.service';
import { UserService } from './services/user.service';
import { throwError } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'project-tracker';
  public user: any;

  constructor(private _userService: UserService){

  }
  ngOnInit(){
    this.user = {
      username: '',
      password: '',

    };
  }
  // login(){
  //   this._userService.login({'username': this.user.username,'password': this.user.password});
  // }
  // refreshToken(){
  //   this._userService.refreshToken();
  // }
  // logout(){
  //   this._userService.logout();
  // }
}


