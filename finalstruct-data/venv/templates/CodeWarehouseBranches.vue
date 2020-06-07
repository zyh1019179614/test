<style scoped>
.card {
  width: 90%;
  margin: 20px auto;
}
.branchtitle {
  float: left;
  background-color: #bad6f1;
  color: #5280e9;
  font-size: 14px;
  width: 60px;
  text-align: center;
}
.branchtime {
  float: left;
  font-size: 14px;
  margin-left: 10px;
}
.branchbutton {
  float: right;
}
.compare {
  float: left;
  margin-left:30%;
  width: 220px;
}
.compareleft {
  float: left;
  text-align: right;
  width: 100px;
}
.compareright {
  float: left;
  text-align: left;
  width: 100px;
}
</style>
<template>
  <div>
    <Card class="card">
      <p slot="title">默认分支</p>
      <div style="height:20px">
        <div class="branchtitle">master</div>
        <div class="branchtime">更新于 1 个月前</div>
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px">下载</Button>
          <Button type="error" style="font-size:12px">删除</Button>
        </ButtonGroup>
      </div>
    </Card>
    <Card class="card">
      <p slot="title">其他分支</p>
      <div style="height:20px">
        <div class="branchtitle">branch1</div>
        <div class="branchtime">更新于 1 个月前</div>
        <!--更新对比-->
        <div class="compare">
          <Tooltip content="比默认分支多1个提交">
            <div class="compareleft">0</div>
            <div style="float:left">
          <Divider type="vertical" /></div>
          <div class="compareright">1</div>
          </Tooltip>
        </div>
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px">下载</Button>
          <Button type="error" style="font-size:12px">删除</Button>
        </ButtonGroup>
      </div>
      <!--分割线-->
      <Divider />
      <div style="height:20px">
        <div class="branchtitle">branch2</div>
        <div class="branchtime">更新于 1 个月前</div>
         <!--更新对比-->
        <div class="compare">
          <Tooltip content="无变化">
            <div class="compareleft">0</div>
            <div style="float:left">
          <Divider type="vertical" /></div>
          <div class="compareright">0</div>
          </Tooltip>
        </div>
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px">下载</Button>
          <Button type="error" style="font-size:12px">删除</Button>
        </ButtonGroup>
      </div>
      <!--分割线-->
      <Divider />
      <div style="height:20px">
        <div class="branchtitle">test1</div>
        <div class="branchtime">更新于 1 个月前</div>
         <!--更新对比-->
        <div class="compare">
          <Tooltip content="比默认分支多12个提交">
            <div class="compareleft">0</div>
            <div style="float:left">
          <Divider type="vertical" /></div>
          <div class="compareright">12</div>
          </Tooltip>
        </div>
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px">下载</Button>
          <Button type="error" style="font-size:12px">删除</Button>
        </ButtonGroup>
      </div>
      <!--分割线-->
      <Divider />
      <div style="height:20px">
        <div class="branchtitle">test2</div>
        <div class="branchtime">更新于 1 个月前</div>
         <!--更新对比-->
        <div class="compare">
          <Tooltip content="比默认分支少11个提交">
            <div class="compareleft">11</div>
            <div style="float:left">
          <Divider type="vertical" /></div>
          <div class="compareright">0</div>
          </Tooltip>
        </div>
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px">下载</Button>
          <Button type="error" style="font-size:12px">删除</Button>
        </ButtonGroup>
      </div>
    </Card>
  </div>
</template>
<script>
export default {};
</script>
