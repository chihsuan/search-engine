class CreateDocLookups < ActiveRecord::Migration
  def change
    create_table :doc_lookups do |t|
      t.integer :doc_id
      t.string :title
      t.float :tf
      t.timestamps
    end
  end
end
