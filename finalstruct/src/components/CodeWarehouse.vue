<style scoped>
.codewarehouse {
  background-color: white;
  height: 350vh;
  overflow-y: hidden;
  width: 100%;
}
</style>
<template>
  <div class="codewarehouse">
    <Menu
      mode="horizontal"
      :theme="light"
      active-name="activemenu"
      @on-select="onMenuSelect"
      style="padding-left: 30%;"
    >
      <MenuItem name="git" :to="{name: 'git'}">代码浏览</MenuItem>
      <MenuItem name="branches" :to="{name: 'branches'}">分支管理</MenuItem>
      <MenuItem name="merge" :to="{name: 'merge'}">合并请求</MenuItem>
      <MenuItem name="version" :to="{name: 'version'}">代码版本</MenuItem>
    </Menu>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  data() {
    return {
      activemenu: git
    };
  },
  // methods: {
  //   menuList() {
  //     // 这个方法里定义好，高亮和路由
  //     let path = this.$route.matched[6].path; // 获取到地址拦上#号后面的url地址
  //     if (path.indexOf("git") != -1) {
  //       // 是否包含，-1是包含，0不包含
  //       this.activemenu = 1;
  //     }else if(path.indexOf("branch") != -1) {
  //       // 是否包含，-1是包含，0不包含
  //       this.activemenu = 2;
  //     }else if(path.indexOf("merge") != -1) {
  //       // 是否包含，-1是包含，0不包含
  //       this.activemenu = 3;
  //     }else if(path.indexOf("version") != -1) {
  //       // 是否包含，-1是包含，0不包含
  //       this.activemenu = 4;
  //     }
  //   }
  // },
  // mounted() {
  //   // 组件初始化后执行
  //   this.menuList();
  // }
};
</script>
