<style scoped>
.content {
  background-color: white;
  height: 200vh;
  overflow-y: hidden;
  overflow-x: hidden;
  width: 100%;
}
.statstitle {
  width: 100%;
  margin-top: 2%;
  margin-bottom: 1%;
  margin-left: 5%;
  font-size: 20px;
  font-weight: bold;
}
.substatstitle {
  width: 90%;
  margin-top: 2%;
  margin-bottom: 2%;
  margin-left: 2%;
  font-size: 17px;
  color: #024ecc;
}
</style>
<template>
  <div class="content">
    <div class="statstitle">本月代码排行</div>
    <Row>
      <Col span="11" offset="1">
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />提交代码次数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="500"
      :columns="columns1"
      :data="data1"
      style="margin-left:2%"
    ></Table>
    </Col>
    <Col span="12">
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />修改代码行数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="500"
      :columns="columns2"
      :data="data2"
      style="margin-left:2%"
    ></Table>
    </Col>
    </Row>
    <Row>
      <Col span="11" offset="1">
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />版本发布次数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="500"
      :columns="columns3"
      :data="data3"
      style="margin-left:2%"
    ></Table>
    </Col>
    <Col span="12">
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />合并请求次数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="500"
      :columns="columns4"
      :data="data4"
      style="margin-left:2%"
    ></Table>
    </Col>
    </Row>
  </div>
</template>
<script>
export default {
  data() {
    return {
      columns1: [
        {
          title: "组名",
          key: "name"
        },
        {
          title: "提交次数",
          key: "committime",
          sortable: true
        }
      ],
      columns2: [
        {
          title: "组名",
          key: "name"
        },
        {
          title: "修改次数",
          key: "changetime",
          sortable: true
        }
      ],
      columns3: [
        {
          title: "组名",
          key: "name"
        },
        {
          title: "版本发布次数",
          key: "submittime",
          sortable: true
        }
      ],
      columns4: [
        {
          title: "组名",
          key: "name"
        },
        {
          title: "请求次数",
          key: "requesttime",
          sortable: true
        }
      ],
      data1: [],
      data2: [],
      data3: [],
      data4: []
    };
  },
  beforeCreate() {
    this.$http
      .get("../static/finalstruct/itemdata.json")
      .then(res => {
        var itemid = this.$route.params.itemID;
        var temp=res.body["commit"][0];
        this.data1 = temp[itemid];
        var temp=res.body["change"][0];
        this.data2 = temp[itemid];
        var temp=res.body["submit"][0];
        this.data3 = temp[itemid];
        var temp=res.body["request"][0];
        this.data4 = temp[itemid];
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
