import { Component, OnInit } from '@angular/core';

import { AuthService } from '../_services/auth.service';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {


  error: any;


  constructor() { }

  ngOnInit(): void {
  }


  signup(username: string,email: string,password1: string, password2: string){
    
  }


}
