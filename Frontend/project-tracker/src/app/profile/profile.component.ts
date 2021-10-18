import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../services/profile.service';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})

export class ProfileComponent implements OnInit {
  profile: any;
  user: any;
  constructor(private PfService: ProfileService, private UDService: UserService) { }

  ngOnInit(): void {
    this.MyData();
    this.MyProfile();
  }

  MyData() {
    this.UDService.getUser().subscribe(user => {
      this.user = user;
      console.log(this.user);
    })
  }

  MyProfile() {
    this.PfService.getProfile().subscribe(profile => {
      this.profile = profile;
      console.log(this.profile);
    })
  }

}
