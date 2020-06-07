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
          <Select v-model="modelstate" style="width:100px" placeholder="全部状态">
            <Option v-for="item in stateList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </Col>
        <Divider type="vertical" />
        <Col span="3">
          <div class="selecttitle">目标分支</div>
          <Select v-model="modelbranch" style="width:100px" placeholder="全部分支">
            <Option
              v-for="item in branchList"
              :value="item.value"
              :key="item.value"
            >{{ item.label }}</Option>
          </Select>
        </Col>
        <Divider type="vertical" />
        <Col span="3">
          <div class="selecttitle">发起者</div>
          <Select v-model="modelpeople" style="width:100px" placeholder="全部成员">
            <Option
              v-for="item in peopleList"
              :value="item.value"
              :key="item.value"
            >{{ item.label }}</Option>
          </Select>
        </Col>
        <Col span="3" offset="10">
          <div style="float:left" class="selecttitle">按创建时间排序</div>
          <Icon
            class="selecttitle"
            size="30"
            type="ios-arrow-round-up"
            v-if="select=='up'"
            style="float:left"
            @click="changetodown"
          />
          <Icon
            class="selecttitle"
            size="30"
            type="ios-arrow-round-down"
            v-else-if="select=='down'"
            style="float:left"
            @click="changetoup"
          />
        </Col>
      </Row>
    </div>
    <div class="versioncontent">
      
      
      <Card dis-hover>
        <div style="padding:10px">
          <div class="topcard">
            <Icon
              type="md-git-pull-request"
              size="25"
              color="blue"
              style="float:left;margin-right:10px"
              class="topcard"
            />
            <div class="topcard" style="font-size:14px;float:left;font-weight:bold">
              <a class="a">test1</a>
            </div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <Avatar size="25" style="margin-right:10px;float:left">U</Avatar>
              <div style="font-size:13px;float:left">主账号创建</div>
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
            <div style="font-size:13px;float:left" class="bottomcard">2020年3月1日</div>
            <div style="margin-left:10px;font-size:12px;float:left">
              test1
              <Icon type="ios-arrow-round-forward" />master
            </div>
          </div>
        </div>
      </Card>
<Divider/>
      <Card dis-hover>
        <div style="padding:10px">
          <div class="topcard">
            <Icon
              type="md-git-pull-request"
              size="25"
              color="blue"
              style="float:left;margin-right:10px"
              class="topcard"
            />
            <div class="topcard" style="font-size:14px;float:left;font-weight:bold">
              <a class="a">test2</a>
            </div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <Avatar size="25" style="margin-right:10px;float:left">U</Avatar>
              <div style="font-size:13px;float:left">主账号创建</div>
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
            <div style="font-size:13px;float:left" class="bottomcard">2020年3月5日</div>
            <div style="margin-left:10px;font-size:12px;float:left">
              branch1
              <Icon type="ios-arrow-round-forward" />master
            </div>
          </div>
        </div>
      </Card>
      <Divider/>
      <Card dis-hover>
        <div style="padding:10px">
          <div class="topcard">
            <Icon
              type="md-git-pull-request"
              size="25"
              color="blue"
              style="float:left;margin-right:10px"
              class="topcard"
            />
            <div class="topcard" style="font-size:14px;float:left;font-weight:bold">
              <a class="a">test3</a>
            </div>
            <div class="topcard" style="float:right;color:grey;margin-right:10px">
              <Avatar size="25" style="margin-right:10px;float:left">U</Avatar>
              <div style="font-size:13px;float:left">主账号创建</div>
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
            <div style="font-size:13px;float:left" class="bottomcard">2020年4月1日</div>
            <div style="margin-left:10px;font-size:12px;float:left">
              brach2
              <Icon type="ios-arrow-round-forward" />master
            </div>
          </div>
        </div>
      </Card>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      stateList: [
        {
          value: "Total",
          label: "全部"
        },
        {
          value: "have",
          label: "已发布"
        },
        {
          value: "will",
          label: "未发布"
        }
      ],
      modelstate: "",
      branchList: [
        {
          value: "master",
          label: "master"
        },
        {
          value: "test1",
          label: "test1"
        }
      ],
      modelbranch: "",
      peopleList: [
        {
          value: "user1",
          label: "user1"
        },
        {
          value: "user2",
          label: "user2"
        },
        {
          value: "user3",
          label: "user3"
        }
      ],
      modelpeople: "",
      select: "up"
    };
  },
  methods: {
    changetodown: function() {
      this.select = "down";
      this.$forceUpdate();
    },
    changetoup: function() {
      this.select = "up";
      this.$forceUpdate();
    }
  }
};
</script>
