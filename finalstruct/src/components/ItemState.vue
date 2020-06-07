<style scoped>
.itemstate {
  background-color: white;
  height: 200vh;
  overflow-y: hidden;
  width: 100%;
}
.timeline {
  margin-left: 8%;
  margin-top: 20px;
}
.subtitle {
  margin-left: 7%;
  margin-top: 20px;
  font-size: 20px;
  font-weight: bold;
}
.time {
  font-size: 12px;
  margin-left: 10%;
}
.content {
  font-size: 14px;
}
.subcontent {
  font-size: 12px;
  color: grey;
}
.name{
  font-size: 14px;
  font-weight: bold;
  color:#0080ff;
  margin-right: 2px;
}
</style>
<template>
  <div class="itemstate">
    <div class="subtitle">项目标题</div>
    <div class="timeline">
      <Timeline v-for="(commit,index) in commitlist" :key="index">
        <TimelineItem color="blue">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">{{commit.created_at}}</p>
            </Col>
            <Col span="18">
              <div><span class="name">{{commit.name}}</span><span class="content">{{commit.title}}</span></div>
              <div class="subcontent">{{commit.message}}</div>
            </Col>
          </Row>
        </TimelineItem>

      </Timeline>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      commitlist: []
    };
  },
  beforeCreate() {
    axios
      .get("/project/commitlist", {
        params: { itemid: this.$route.params.itemID },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.commitlist = res.data;
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
