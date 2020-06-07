<style scoped>
.card {
  width: 90%;
  margin: 20px auto;
}
.branchtitle {
  font-size: 14px;
  font-weight: bold;
  margin-left: 10px;
  margin-bottom: 5px;
}
.branchtime {
  font-size: 14px;
  margin-left: 10px;
}
.branchbutton {
  float: right;
}
.compare {
  float: left;
  margin-left: 30%;
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
.mergebutton {
  font-size: 12px;
  height: 20px;

  margin-left: 6px;
  text-align: center;
}
</style>
<template>
  <div>
    <!-- 主分支 -->
    <Card class="card" v-for="(branch,index) in branchmaster" :key="index">
      <p slot="title">默认分支</p>
      <div style="height:40px">
        <div style="float:left">
          <div class="branchtitle">
            <Icon type="md-git-network" />
            {{branch.name}}
            <Button
              type="primary"
              class="mergebutton"
              style="width:70px;"
              v-if="branch.merged"
            >merged</Button>
            <Button type="success" class="mergebutton" style="width:83px;" v-else>unmerged</Button>
          </div>
          <div class="branchtime">
            <Icon type="md-git-commit" />
            <span style="color:#0080ff">{{branch.commit_short_id}}·</span>
            <span style="font-weight:bold">{{branch.commit_title}}·</span>
            {{branch.commit_created_at}}
          </div>
        </div>
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px" @click="downloadBranch()">下载</Button>
          <Button type="error" style="font-size:12px" disabled>删除</Button>
        </ButtonGroup>
      </div>
    </Card>
    <Card class="card" v-for="(branch,index) in branchlist" :key="index">
      <div style="height:40px">
        <div style="float:left">
          <div class="branchtitle">
            <Icon type="md-git-network" />
            {{branch.name}}
            <Button
              type="primary"
              class="mergebutton"
              style="width:70px;"
              v-if="branch.merged"
            >merged</Button>
            <Button type="success" class="mergebutton" style="width:83px;" v-else>unmerged</Button>
          </div>
          <div class="branchtime">
            <Icon type="md-git-commit" />
            <span style="color:#0080ff">{{branch.commit_short_id}}·</span>
            <span style="font-weight:bold">{{branch.commit_title}}·</span>
            {{branch.commit_created_at}}
          </div>
        </div>
        <!--更新对比-->
        <!-- <div class="compare">
          <Tooltip content="比默认分支多1个提交">
            <div class="compareleft">0</div>
            <div style="float:left">
              <Divider type="vertical" />
            </div>
            <div class="compareright">1</div>
          </Tooltip>
        </div>-->
        <ButtonGroup class="branchbutton" size="small">
          <Button type="success" style="font-size:12px" @click="downloadBranch()">下载</Button>
          <Button type="error" style="font-size:12px" @click="deleteBranch(branch.name)">删除</Button>
        </ButtonGroup>
      </div>
    </Card>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "projectbranchlist",
  data() {
    return {
      branchlist: [],
      branchmaster: []
    };
  },
  methods: {
    deleteBranch: function(name) {
      this.$Modal.confirm({
        title: "确认",
        content: "<p>是否确认删除该分支？</p>",
        onOk: () => {
          axios
            .get("/project/branchdelete", {
              params: { itemid: this.$route.params.itemID, branchname: name },
              headers: { "Access-Control-Allow-Origin": "*" }
            })
            .then(res => {
              console.log(res.data);
              this.$Message.info("删除成功！");
              location.reload();
            })
            .catch(err => {
              console.error(err);
            });
        },
        onCancel: () => {
          this.$Message.info("Clicked cancel");
        }
      });
    },
    downloadBranch: function() {
      var url = "http://127.0.0.1:5000/project/branchdownload";
      window.open(url);
    }
  },
  created() {
    axios
      .get("/project/branchlist", {
        params: { itemid: this.$route.params.itemID },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.branchlist = res.data;
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  },
  beforeCreate() {
    axios
      .get("/project/branchmaster", {
        params: { itemid: this.$route.params.itemID },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.branchmaster = res.data;
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
