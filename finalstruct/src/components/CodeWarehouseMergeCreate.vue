<style scoped>
.selectlist {
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: center;
}
.selecttitle {
  float: left;
  height: 35px;
  line-height: 35px;
}
.code-row-bg {
  height: 35px;
  line-height: 35px;
}
.a {
  text-decoration: none;
  color: #000;
}
.titletext {
  margin-left: 2.5%;
  margin-right: 1.5%;
  margin-top: 10px;
  margin-bottom: 10px;
}
.mergetext {
  width: 96%;
  height: 100%;
  margin-left: 2.5%;
  margin-right: 1.5%;
  border: 1px solid #d9d9d9;
  padding: 1%;
}

.button {
  font-size: 12px;
  margin-top: 10px;
}
</style>
<template>
  <div>
    <div class="titletext">
      <h2>新建合并请求</h2>请选择合并请求的源分支和目标分支
      <br />合并之后目标分支将会包括源分支的改动内容
    </div>
    <!--选择合并源和目标-->
    <div class="selectlist">
      <Row type="flex" justify="start" align="middle" class="code-row-bg">
        <Col span="10" offset="1">
          <div class="selecttitle">源分支</div>
          <Select v-model="modelsource" style="width:450px" placeholder="master" @on-change="choosesource">
            <Option
              v-for="item in branchList"
              :value="item.value"
              :key="item.value"
            >{{ item.label }}</Option>
          </Select>
        </Col>

        <Col span="2">>>合并到>></Col>
        <Col span="10" offset="1">
          <div class="selecttitle">目标分支</div>
          <Select v-model="modeltarget" style="width:450px" placeholder="master" @on-change="choosetarget">
            <Option
              v-for="item in branchList"
              :value="item.value"
              :key="item.value"
            >{{ item.label }}</Option>
          </Select>
        </Col>
      </Row>
    </div>
    <!--填写合并内容-->
    <div class="mergetext">
      <div>
        <div style="font-size:20px;margin:10px">标题</div>
        <Input v-model="titlemodel" placeholder="请输入请求标题" style="width: 100%"  @on-blur="gettitle"/>
      </div>
      <div>
        <div style="font-size:20px;margin:10px">描述</div>
        <div style="border: 0.5px solid #d9d9d9;height:100%;">
          <i-editor v-model="content" style="height:100%;" :autosize="{minRows: 10,maxRows: 10}" @on-enter="getdescription"></i-editor>
        </div>
      </div>
      <Button class="button" type="primary" @click="createmerge">新建合并请求</Button>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      branchList: [],
      modelsource: "",
      modeltarget: "",
      content: "",
      title:"",
      titlemodel:"",
    };
  },
  methods: {
    choosesource(value){
      this.modelsource=value;
    },
    choosetarget(value){
      this.modeltarget=value;
    },
    gettitle(){
      this.title=this.titlemodel;
    },
    getdescription(value){
      this.content=value;
    },
    createmerge(){
      axios
      .get("/project/mergecreate", {
        params: { 
          itemid: this.$route.params.itemID ,
          sourcebranch:this.modelsource ,
          targetbranch:this.modeltarget ,
          title:this.title,
          description:this.content ,
          },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.$Modal.success({
                            title: "创建成功",
                            content: res.data,
                        });
        this.$router.push({
          path: 'merge'
        })                
      })
      .catch(err => {
        this.$Modal.error({
                            title: "创建失败",
                            content: err.response.data,
                        });
        console.error(err.response);
      });
    }
  },
  beforeCreate() {
    axios
      .get("/project/branchlistall", {
        params: { itemid: this.$route.params.itemID },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.branchList = res.data;
        console.log(this.branchList);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
