<template>
  <div id="index">
    <Menu mode="horizontal" theme="dark" active-name="1" style="z-index:999">
      <MenuItem name="logo" style="width: 200px;text-align:center;font-size:22px">协同云教学平台</MenuItem>
      <MenuItem name="papers" :to="{name: 'Upapers'}">
        <Dropdown>
            <a href="javascript:void(0)" style="color:white">
                项目列表
                <Icon type="ios-arrow-down"></Icon>
            </a>
            <DropdownMenu slot="list">
                <DropdownItem>项目一</DropdownItem>
                <DropdownItem>项目二</DropdownItem>
                <DropdownItem>项目三</DropdownItem>
                <DropdownItem>项目四</DropdownItem>
                <DropdownItem>项目五</DropdownItem>
            </DropdownMenu>
        </Dropdown>
      </MenuItem>
      <MenuItem name="userspace" style="float:right">
        <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
        <Dropdown>
            <a href="javascript:void(0)" style="color:black">
                <Icon type="ios-arrow-down"></Icon>
            </a>
            <DropdownMenu slot="list">
                <DropdownItem>我的团队</DropdownItem>
                <DropdownItem>设置</DropdownItem>
                <DropdownItem>退出</DropdownItem>
            </DropdownMenu>
        </Dropdown>
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
      keywords: "",
    };
  },
  methods: {
  }
};
</script>
