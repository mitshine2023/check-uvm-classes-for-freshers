
class txn1 extends uvm_sequence_item;

`uvm_component_utils(txn1)

constraint addr {addr > 0; addr < 10};

soft constraint data {data inside [0:100]};

assert.randomize(txn1);

endclass