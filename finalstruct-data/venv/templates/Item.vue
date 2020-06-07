<style scoped>
.layout {
  background: #fff;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
  height: 100%;
}
.menu-item span {
  display: inline-block;
  overflow: hidden;
  width: 69px;
  text-overflow: ellipsis;
  white-space: nowrap;
  vertical-align: bottom;
  transition: width 0.2s ease 0.2s;
}
.menu-item i {
  transform: translateX(0px);
  transition: font-size 0.2s ease, transform 0.2s ease;
  vertical-align: middle;
  font-size: 16px;
}
.collapsed-menu span {
  width: 0px;
  transition: width 0.2s ease;
}
.collapsed-menu i {
  transform: translateX(5px);
  transition: font-size 0.2s ease 0.2s, transform 0.2s ease 0.2s;
  vertical-align: middle;
  font-size: 22px;
}
.sider {
  display: block;
  background: #fff;
  left: 0;
  bottom: 0;
  border: 1px;
}
</style>
<template>
  <div class="layout">
    <Layout style="background: #fff; height:100%; ">
      <Sider breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed">
        <Menu
          active-name="1-1"
          theme="dark"
          width="auto"
          :class="menuitemClasses"
          style="border:0px"
        >
          <MenuItem name="1-1" :to="{name: 'itemstate'}">
            <Icon type="ios-navigate"></Icon>
            <span>项目动态</span>
          </MenuItem>
          <MenuItem name="1-2" :to="{name: 'codewarehouse'}">
            <Icon type="ios-search"></Icon>
            <span>代码仓库</span>
          </MenuItem>
          <Submenu name="3">
            <template slot="title">
              <Icon type="ios-analytics" />统计
            </template>
              <MenuItem name="3-1" :to="{name: 'betweengroup'}">组间数据统计</MenuItem>
              <MenuItem name="3-2" :to="{name: 'intragroup'}">组内数据统计</MenuItem>
          </Submenu>
        </Menu>
        <div slot="trigger"></div>
      </Sider>
      <Layout>
        <router-view></router-view>
      </Layout>
    </Layout>
  </div>
</template>
<script>
export default {
  name: "item",
  data() {
    return {
      isCollapsed: false
    };
  },
  computed: {
    menuitemClasses: function() {
      return ["menu-item", this.isCollapsed ? "collapsed-menu" : ""];
    }
  }
};
</script>
