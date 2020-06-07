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
  margin-left: 2%;
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
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />提交代码次数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="1200"
      :columns="columns1"
      :data="data1"
      style="margin-left:2%"
    ></Table>
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />修改代码行数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="1200"
      :columns="columns2"
      :data="data2"
      style="margin-left:2%"
    ></Table>
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />版本发布次数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="1200"
      :columns="columns3"
      :data="data3"
      style="margin-left:2%"
    ></Table>
    <div class="substatstitle">
      <Icon type="md-list" color="#024ecc" />合并请求次数
    </div>
    <Table
      highlight-row
      border
      height="250"
      width="1200"
      :columns="columns4"
      :data="data4"
      style="margin-left:2%"
    ></Table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      columns1: [
        {
          title: "排名",
          key: "submitnum",
          sortable: true
        },
        {
          title: "组名",
          key: "name"
        },
        {
          title: "提交次数",
          key: "submittime",
          sortable: true
        }
      ],
      columns2: [
        {
          title: "排名",
          key: "submitnum",
          sortable: true
        },
        {
          title: "组名",
          key: "name"
        },
        {
          title: "修改次数",
          key: "submittime",
          sortable: true
        }
      ],
      columns3: [
        {
          title: "排名",
          key: "submitnum",
          sortable: true
        },
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
          title: "排名",
          key: "submitnum",
          sortable: true
        },
        {
          title: "组名",
          key: "name"
        },
        {
          title: "请求次数",
          key: "submittime",
          sortable: true
        }
      ],
      data1: [
        {
          submitnum: 1,
          name: "Group test",
          submittime: 340
        },
        {
          submitnum: 2,
          name: "Group two",
          submittime: 2
        },
        {
          submitnum: 3,
          name: "Group four",
          submittime: 1
        },
        {
          submitnum: 4,
          name: "Group five",
          submittime: 0
        },
        {
          submitnum: 5,
          name: "Group three",
          submittime: 0
        },
      ],
      data2: [
        {
          submitnum: 1,
          name: "Group test",
          submittime: 789
        },
        {
          submitnum: 2,
          name: "Group two",
          submittime: 2
        },
        {
          submitnum: 3,
          name: "Group four",
          submittime: 0
        },
        {
          submitnum: 4,
          name: "Group five",
          submittime: 0
        },
        {
          submitnum: 5,
          name: "Group three",
          submittime: 0
        },
      ],
      data3: [
        {
          submitnum: 1,
          name: "Group test",
          submittime: 0
        },
        {
          submitnum: 2,
          name: "Group two",
          submittime: 0
        },
        {
          submitnum: 3,
          name: "Group four",
          submittime: 0
        },
        {
          submitnum: 4,
          name: "Group five",
          submittime: 0
        },
        {
          submitnum: 5,
          name: "Group three",
          submittime: 0
        },
      ],
      data4: [
        {
          submitnum: 1,
          name: "Group test",
          submittime: 3
        },
        {
          submitnum: 2,
          name: "Group two",
          submittime: 0
        },
        {
          submitnum: 3,
          name: "Group four",
          submittime: 0
        },
        {
          submitnum: 4,
          name: "Group five",
          submittime: 0
        },
        {
          submitnum: 5,
          name: "Group three",
          submittime: 0
        },
      ]
    };
  }
};
</script>
