<template>
  <div style="width:80%;margin-left:10%;margin-right:10%">
    <Card dis-hover style="text-align:center">
      <p slot="title">邀请成员加入团队</p>
      <Button type="primary" @click="modal1 = true">添加成员</Button>
      <Button @click="modal2 = true">移除成员</Button>
      <!--添加成员弹窗-->
      <Modal v-model="modal1" title="添加成员" @on-ok="ok" @on-cancel="cancel">
        <Input search placeholder="搜索..." />
        <Table border ref="selection" :columns="columns2" :data="data2" style="margin-top:10px;margin-bottom:10px"></Table>
        <Button @click="handleSelectAll(true)">全选</Button>
        <Button @click="handleSelectAll(false)">取消全选</Button>
      </Modal>
      <!--移除成员弹窗-->
      <Modal v-model="modal2" title="移除成员" @on-ok="ok" @on-cancel="cancel">
        <Input search placeholder="搜索..." />
        <Table border ref="selection" :columns="columns2" :data="data2" style="margin-top:10px;margin-bottom:10px"></Table>
        <Button @click="handleSelectAll(true)">全选</Button>
        <Button @click="handleSelectAll(false)">取消全选</Button>
      </Modal>
    </Card>
    <Table :columns="columns1" :data="data1"></Table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      modal1: false,
      modal2: false,
      columns1: [
        {
          title: "成员姓名",
          key: "name"
        },
        {
          title: "所属用户组",
          key: "group"
        },
        {
          title: "邮箱",
          key: "email"
        }
      ],
      data1: [
        {
          name: "zyh",
          group: "团队所有者",
          email: "1019179614@qq.com"
        }
      ],
      columns2: [
        {
          type: "selection",
          width: 60,
          align: "center"
        },
        {
          title: "姓名",
          key: "name"
        },
        {
          title: "学号",
          key: "age"
        },
        {
          title: "邮箱",
          key: "address"
        }
      ],
      data2: [
        {
          name: "John Brown",
          age: 18,
          address: "New York No. 1 Lake Park",
        },
        {
          name: "Jim Green",
          age: 24,
          address: "London No. 1 Lake Park",
        },
        {
          name: "Joe Black",
          age: 30,
          address: "Sydney No. 1 Lake Park",
        },
        {
          name: "Jon Snow",
          age: 26,
          address: "Ottawa No. 2 Lake Park",
        }
      ]
    };
  },
  methods: {
    ok() {
      this.$Message.info("Clicked ok");
    },
    cancel() {
      this.$Message.info("Clicked cancel");
    },
    handleSelectAll(status) {
      this.$refs.selection.selectAll(status);
    }
  }
};
</script>
