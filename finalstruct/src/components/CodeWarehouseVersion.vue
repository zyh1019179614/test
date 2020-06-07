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
  /* color: #33ff33 */
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
          <div class="selecttitle">发布状态</div>
          <Select
            v-model="modelstate"
            style="width:100px"
            placeholder="全部状态"
            @on-change="choosestate"
          >
            <Option v-for="item in stateList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </Col>
        <Divider type="vertical" />
        <Col span="7">
          <div class="selecttitle">创建日期</div>
          <DatePicker
            type="date"
            placement="bottom-end"
            placeholder="开始时间"
            style="width: 150px"
            v-model="starttime"
            @on-change="startTimeChange"
          ></DatePicker>
          <DatePicker
            type="date"
            placement="bottom-end"
            placeholder="结束时间"
            style="width: 150px"
            v-model="endtime"
            @on-change="endTimeChange"
          ></DatePicker>
        </Col>
      </Row>
    </div>
    <div class="versioncontent">
      <Card style="margin-bottom:20px" dis-hover v-for="(issue,index) in issuelist" :key="index">
        <div style="padding:10px;">
          <div class="topcard">
            <Icon
              type="md-code"
              size="25"
              color="blue"
              style="float:left;margin-right:10px"
              class="topcard"
              v-if="issue.state == 'closed'"
            />
            <Icon
              type="md-code"
              size="25"
              color="#33ff33"
              style="float:left;margin-right:10px"
              class="topcard"
              v-else
            />
            <div class="topcard" style="font-size:14px;float:left;font-weight:bold">
              <span >#{{issue.iid}} </span>
              <span class="a" @click="getissuedetail(issue.iid)">{{issue.title}}</span>
            </div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <div style="font-size:13px;float:left;font-weight:bold">{{issue.author}}·创建</div>
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
            <div style="font-size:13px;float:left" class="bottomcard">更新于·{{issue.updated_at}}·</div>
            <div
              style="margin-left:10px;font-size:12px;float:left"
            >{{issue.task_completed}} of {{issue.task_num}} tasks completed</div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <div style="font-size:13px;float:left">{{issue.created_at}}</div>
            </div>
          </div>
        </div>
      </Card>
      <Divider />
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      issuelist: [],
      stateList: [
        {
          value: "all",
          label: "全部"
        },
        {
          value: "closed",
          label: "已发布"
        },
        {
          value: "opened",
          label: "未发布"
        }
      ],
      modelstate: "",
      starttime: "2000-1-1", //开始日期model
      endtime: "2020-5-31", //结束日期model
      state: "all",
      startstatictime :"2000-1-1",
      endstatictime: "2020-5-31"
    };
  },
  methods: {
    p(s) {
      return s < 10 ? '0' + s : s
    },
    staticstarttime(){
      this.starttime =new Date(this.starttime);
      this.startstatictime=this.starttime.getFullYear() + '-' + this.p((this.starttime.getMonth() + 1)) + '-' + this.p(this.starttime.getDate());
    },
    staticendtime(){
      this.endtime =new Date(this.endtime);
      this.endstatictime=this.endtime.getFullYear() + '-' + this.p((this.endtime.getMonth() + 1)) + '-' + this.p(this.endtime.getDate());
    },
    startTimeChange: function(value) {
      this.starttime = value;
      this.staticstarttime();
      axios
        .get("/project/issuelist", {
          params: {
            itemid: this.$route.params.itemID,
            state: this.state,
            created_after: this.startstatictime,
            created_before: this.endstatictime,
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.issuelist = res.data;
          console.log(res.data);
        })
        .catch(err => {
          console.error(err);
        });
    },
    endTimeChange: function(value) {
      this.endtime = value;
      this.staticendtime();
      axios
        .get("/project/issuelist", {
          params: {
            itemid: this.$route.params.itemID,
            state: this.state,
            created_after: this.startstatictime,
            created_before: this.endstatictime,
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.issuelist = res.data;
          console.log(res.data);
        })
        .catch(err => {
          console.error(err);
        });
    },
    choosestate(value) {
      this.state = value;
      this.staticstarttime();
      this.staticendtime();
      axios
        .get("/project/issuelist", {
          params: {
            itemid: this.$route.params.itemID,
            state: this.state,
            created_after: this.startstatictime,
            created_before: this.endstatictime,
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.issuelist = res.data;
          console.log(res.data);
        })
        .catch(err => {
          console.error(err);
        });
    },
    getissuedetail(iid){
      this.$router.push({
          path: 'versiondetail',
          query: {
            iid:iid
          }
        })
    }
  },
  beforeCreate() {
    axios
      .get("/project/issuelist", {
        params: {
          itemid: this.$route.params.itemID,
          state: "all",
          created_after: "2000-1-1",
          created_before: "2020-5-31",
        },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.issuelist = res.data;
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
