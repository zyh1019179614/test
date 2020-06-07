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
  width: 120px;
  text-align: center;
  margin-right: 10px;
}
.branchtitlered {
  float: left;
  background-color: #ffe8df;
  color: red;
  font-size: 14px;
  width: 120px;
  text-align: center;
  margin-right: 10px;
}
.branchtitleblue {
  border-radius: 5px;
  float: left;
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
      >{{this.detail.merge_status}}</div>
      <div class="branchtitlered" v-else>{{this.detail.merge_status}}</div>
      <div style="float:left;">
        <div class="branchtitleblue">{{this.detail.source_branch}}</div>
        <Icon style="float:left;" type="ios-arrow-round-forward" size="22" />
        <div class="branchtitleblue">{{this.detail.target_branch}}</div>
      </div>
      <Divider />
    </div>
    <div class="branchtext">
      <div>
        <div style="font-size:20px;margin:10px">摘要</div>
        <div style="height:100%;">
          <i-editor v-model="content" style="height:100%;" :autosize="{minRows: 20,maxRows: 20}"></i-editor>
        </div>
      </div>
      <div>
        <div style="font-size:20px;margin:10px">代码对比</div>
        <code-diff :old-string="oldStr" :new-string="newStr" :context="3" />
      </div>
      <Button
        style="margin:10px"
        type="success"
        v-if="this.detail.state == 'opened'"
        @click="merge"
      >合并分支</Button>
      <Button style="margin:10px" type="success" v-else disabled>合并分支</Button>
      <Button style="margin:10px" type="error" @click="mergedelete">删除合并请求</Button>
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
      oldStr: "old code",
      newStr: "new code",
      description: " ",
      outputFormat: "side-by-side"
    };
  },
  methods: {
    success() {
      this.$Message.success("操作成功");
    },
    error() {
      this.$Message.error("操作失败");
    },
    merge() {
      axios
        .get("/project/merge", {
          params: {
            itemid: this.$route.params.itemID,
            mrid: this.$route.query.iid
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
    mergedelete() {
      axios
        .get("/project/mergedelete", {
          params: {
            itemid: this.$route.params.itemID,
            mrid: this.$route.query.iid
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.success();
          this.$router.push({
            path: "merge"
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
      .get("/project/mergedetail", {
        params: {
          itemid: this.$route.params.itemID,
          mrid: this.$route.query.iid
        },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.detailTable = res.data;
        this.detail = this.detailTable[this.$route.query.iid];
        this.oldStr = this.detail.oldcode;
        this.newStr = this.detail.newcode;
        this.content = this.detail.description;

        console.log(this.detail);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
