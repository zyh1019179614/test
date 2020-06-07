<template>
  <div id="index">
    <Menu mode="horizontal" theme="dark" active-name="1" style="z-index:999">
      <MenuItem name="logo" style="width: 200px;text-align:center;font-size:22px">协同云教学平台</MenuItem>
      <MenuItem name="list" v-if="this.$route.params.userID != 0">
        <Dropdown @on-click="toProject">
          <a href="javascript:void(0)" style="color:white">
            项目列表
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list" >
            <DropdownItem name="1">项目一</DropdownItem>
            <DropdownItem name="2">项目二</DropdownItem>
            <DropdownItem name="3">项目三</DropdownItem>
            <DropdownItem name="4">项目四</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </MenuItem>
      <MenuItem name="user" style="float:right">
        <Avatar style="color: #f56a00;background-color: #fde3cf" >{{this.$route.params.userID}}</Avatar>
      </MenuItem>
    </Menu>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "userIndex",
  data() {
    return {
      MenuText: "项目列表",
      menuList: [],
      userid: "",
      isTeacher: false,
      newopen: false
    };
  },
  methods: {
    toProject(name) {
      if(this.userid == 1)
      {
        var patth;
        if(name == 1){patth = 4}
        else if(name == 2){patth = 10}
        else if(name == 3){patth = 11}
        else if(name == 4){patth = 12};
        this.$router.push({
          path: `/user/1/item/${patth}`
        });
        this.$router.go(0);
      }else if(this.userid == 2)
      {
        var patth;
        if(name == 1){patth = 3}
        else if(name == 2){patth = 5}
        else if(name == 3){patth = 6}
        else if(name == 4){patth = 13};
        this.$router.push({
          path: `/user/2/item/${patth}`
        });
        this.$router.go(0);
      }
    }
  },
  beforeCreate() {
    this.$http
      .get("../static/finalstruct/usersearch.json")
      .then(res => {
        this.userid = this.$route.params.userID;
        this.MenuList = JSON.parse(JSON.stringify(res.body[this.userid][0]));
        console.log(this.MenuList);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
