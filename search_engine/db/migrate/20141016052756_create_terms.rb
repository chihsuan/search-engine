class CreateTerms < ActiveRecord::Migration
  def change
    create_table :terms do |t|
      t.string :term
      t.integer :document_count
      t.integer :frequency
      t.timestamps
    end
  end
end
