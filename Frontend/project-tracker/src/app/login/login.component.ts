import { Component, OnInit } from '@angular/core';

import { AuthService } from '../_services/auth.service';
import { TokenStorageService } from '../_services/token-storage.service';
import { FormGroup, FormControl } from '@angular/forms';
import { first } from 'rxjs/operators';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  myForm: FormGroup;
  //data: any;

  constructor(private authService: AuthService,) { }

  ngOnInit(): void {
    this.myForm = new FormGroup({
      email: new FormControl(''),
      password: new FormControl('')
    });
  }

  get f() {
    return this.myForm.controls;
  }

  onSubmit() {
    // this.authService.login(this.f.email.value, this.f.password.value).pipe(first()).subscribe
    //   data() => {
    //     console.log(data);
    //   }
  }
}
