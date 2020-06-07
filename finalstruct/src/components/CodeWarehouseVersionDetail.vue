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
.branchtext {
  height: 100%;
  margin-left: 2.5%;
  margin-right: 1.5%;
}
.branchtitlegreen {
  float: left;
  background-color: #dfffdf;
  color: green;
  font-size: 14px;
  width: 60px;
  text-align: center;
  margin-right: 10px;
}
.branchtitlered {
  float: left;
  background-color: #ffe8df;
  color: red;
  font-size: 14px;
  width: 60px;
  text-align: center;
  margin-right: 10px;
}
.branchtitleblue {
  border-radius: 5px;
  color: #5280e9;
  font-size: 14px;
  text-align: center;
}
.button {
  font-size: 12px;
  margin-top: 10px;
}
</style>
<template>
  <div>
    <div class="titletext">
      <h1>{{this.detail.title}}</h1>
      <br />
      <div
        class="branchtitlegreen"
        v-if="this.detail.state == 'opened'"
      >未发布</div>
      <div class="branchtitlered" v-else>已发布</div>
      <div style="float:left;">
        <span class="branchtitleblue">{{this.detail.task_completed}}</span>
         of 
        <span class="branchtitleblue">{{this.detail.task_num}}</span>
         tasks completed
      </div>
      <Divider />
    </div>
    <div class="branchtext">
      <div>
        <div style="font-size:20px;margin:10px">摘要</div>
        <div style="height:100%;">
          <i-editor v-model="content" style="height:100%;" :autosize="true"></i-editor>
        </div>
      </div>
      <div>
        
      </div>
      <Button
        style="margin:10px"
        type="success"
        v-if="this.detail.state == 'opened'"
        @click="issue"
      >发布版本</Button>
      <Button style="margin:10px" type="success" v-else disabled>发布版本</Button>
      <Button style="margin:10px" type="error" @click="issuedelete">删除版本</Button>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import CodeDiff from "vue-code-diff";
export default {
  components: { CodeDiff },
  data() {
    return {
      detail: [],
      detailTable: [],
      modelstate: "",
      content: "",
      description: " ",
    };
  },
  methods: {
    success() {
      this.$Message.success("操作成功");
    },
    error() {
      this.$Message.error("操作失败");
    },
    issue() {
      axios
        .get("/project/issue", {
          params: {
            itemid: this.$route.params.itemID,
            issueid: this.$route.query.iid
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.success();
          location.reload();
          console.log(res);
        })
        .catch(err => {
          this.error();
          location.reload();
          console.error(err);
        });
    },
    issuedelete() {
      axios
        .get("/project/issuedelete", {
          params: {
            itemid: this.$route.params.itemID,
            issueid: this.$route.query.iid
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.success();
          this.$router.push({
            path: "version"
          });
          console.log(res);
        })
        .catch(err => {
          this.error();
          location.reload();
          console.error(err);
        });
    }
  },
  beforeCreate() {
    axios
      .get("/project/issuedetail", {
        params: {
          itemid: this.$route.params.itemID,
          issueid: this.$route.query.iid
        },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.detailTable = res.data;
        this.detail = this.detailTable[this.$route.query.iid];
        this.content = this.detail.description;
        console.log(this.detail);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
