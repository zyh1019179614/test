<style scoped>
.codewarehouse {
  background-color: white;
  height: 200vh;
  overflow-y:hidden;
  width:100%;
}
</style>
<template>
  <div class="codewarehouse">
    <Menu
      mode="horizontal"
      :theme="light"
      active-name="1"
      @on-select="onMenuSelect"
      style="padding-left: 30%;"
    >
      <MenuItem name="1" :to="{name: 'git'}">代码浏览</MenuItem>
      <MenuItem name="2" :to="{name: 'branches'}">分支管理</MenuItem>
      <MenuItem name="3" :to="{name: 'version'}">代码版本</MenuItem>
      <MenuItem name="4" :to="{name: 'merge'}">合并请求</MenuItem>
    </Menu>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  }
};
</script>
