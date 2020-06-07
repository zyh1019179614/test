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
.versioncontent {
  margin: 20px;
}
.a {
  text-decoration: none;
  color: #000;
}
.topcard {
  height: 25px;
  line-height: 25px;
}
.bottomcard {
  height: 15px;
  line-height: 15px;
}
</style>
<template>
  <div>
    <div class="selectlist">
      <Row type="flex" justify="start" align="middle" class="code-row-bg">
        <Col span="3" offset="1">
          <div class="selecttitle">状态</div>
          <Select
            v-model="modelstate"
            style="width:100px"
            placeholder="全部状态"
            @on-change="choosestate"
          >
            <Option v-for="item in stateList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </Col>
        <Col span="2" offset="17">
          <Button icon="md-add" to="mergecreate">新建合并请求</Button>
        </Col>
      </Row>
    </div>
    <div class="versioncontent">
      <Card style="margin-bottom:20px" dis-hover v-for="(mr,index) in mergelist" :key="index">
        <div style="padding:10px;">
          <div class="topcard">
            <Icon
              type="md-git-pull-request"
              size="25"
              color="blue"
              style="float:left;margin-right:10px"
              class="topcard"
            />
            <div class="topcard" style="font-size:14px;float:left;font-weight:bold">
              <span class="a" @click="getmergedetail(mr.iid)">{{mr.title}}</span>
            </div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <div style="font-size:13px;float:left;font-weight:bold">{{mr.author}}·创建</div>
            </div>
          </div>
          <Divider size="small" />
          <div class="bottomcard" style="padding-left:15px">
            <Icon
              type="md-calendar"
              size="20"
              style="margin-right:10px;float:left"
              class="bottomcard"
            />
            <div style="font-size:13px;float:left" class="bottomcard">更新于·{{mr.updated_at}}·</div>
            <div style="margin-left:10px;font-size:12px;float:left">
              {{mr.source_branch}}
              <Icon type="ios-arrow-round-forward" />{{mr.target_branch}}
            </div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <div style="font-size:13px;float:left">{{mr.created_at}}</div>
            </div>
          </div>
        </div>
      </Card>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      stateList: [
        {
          value: "all",
          label: "全部"
        },
        {
          value: "merged",
          label: "已合并"
        },
        {
          value: "opened",
          label: "开启中"
        },
        {
          value: "closed",
          label: "已关闭"
        }
      ],
      modelstate: "",
      mergelist: [],
      state: "all",
      sort: "asc",
    };
  },
  methods: {
    choosestate(value) {
      this.state = value;
      axios
        .get("/project/mergelist", {
          params: {
            itemid: this.$route.params.itemID,
            state: this.state,
            sort: this.sort
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.mergelist = res.data;
          console.log(res.data);
        })
        .catch(err => {
          console.error(err);
        });
    },
    getmergedetail(iid){
      this.$router.push({
          path: 'mergedetail',
          query: {
            iid:iid
          }
        })
    }
  },
  beforeCreate() {
    axios
      .get("/project/mergelist", {
        params: {
          itemid: this.$route.params.itemID,
          state: "all",
          sort: "asc"
        },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.mergelist = res.data;
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
